import os
import argparse
import torch
import gradio as gr
from transformers import AutoModel, AutoTokenizer, AutoConfig
import mdtex2html

# ---------------------- 命令行参数 ----------------------
parser = argparse.ArgumentParser()
parser.add_argument("--model_name_or_path", type=str, default="THUDM/chatglm2-6b",
                    help="Path to pretrained model or model identifier from HuggingFace hub.")
parser.add_argument("--checkpoint", type=str, default="checkpoint/pytorch_model.bin",
                    help="Path to the prefix-tuning checkpoint file.")
args = parser.parse_args()

# ---------------------- 模型加载 ----------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

config = AutoConfig.from_pretrained(args.model_name_or_path, trust_remote_code=True)
config.pre_seq_len = 128
config.prefix_projection = False

tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path, trust_remote_code=True)
model = AutoModel.from_pretrained(args.model_name_or_path, config=config, trust_remote_code=True)

# 加载 Prefix Encoder 权重
prefix_state_dict = torch.load(args.checkpoint, map_location="cpu")
new_prefix_state_dict = {
    k[len("transformer.prefix_encoder."):]: v
    for k, v in prefix_state_dict.items()
    if k.startswith("transformer.prefix_encoder.")
}
model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)

model.to(device)
model.eval()

# ---------------------- Markdown 渲染 ----------------------
def postprocess(self, y):
    if y is None:
        return []
    for i, (message, response) in enumerate(y):
        y[i] = (
            None if message is None else mdtex2html.convert(message),
            None if response is None else mdtex2html.convert(response),
        )
    return y

gr.Chatbot.postprocess = postprocess

def parse_text(text):
    lines = [line for line in text.split("\n") if line]
    count = 0
    for i, line in enumerate(lines):
        if "```" in line:
            count += 1
            lines[i] = "<pre><code>" if count % 2 == 1 else "</code></pre>"
        else:
            if count % 2 == 1:
                line = (line.replace("&", "&amp;")
                            .replace("<", "&lt;")
                            .replace(">", "&gt;")
                            .replace(" ", "&nbsp;"))
            lines[i] = "<br>" + line
    return "".join(lines)

# ---------------------- 推理函数 ----------------------
def predict(user_input, chatbot, history, past_key_values):
    chatbot.append((parse_text(user_input), ""))
    history = []  # 清空历史（如需保留记忆，可修改此处）

    for response, history, past_key_values in model.stream_chat(
        tokenizer,
        user_input,
        history,
        return_past_key_values=True,
        past_key_values=past_key_values
    ):
        chatbot[-1] = (parse_text(user_input), parse_text(response))
        yield chatbot, history, past_key_values

def reset_user_input():
    return gr.update(value='')

def reset_state():
    return [], [], None

# ---------------------- Gradio UI ----------------------
with gr.Blocks(css="#chatbot .overflow-y-auto{height:400px}") as demo:
    gr.HTML("<h1 align='center'>DaiyuLM 🌸<br><small>林黛玉式情绪对话生成模型</small></h1>")

    chatbot = gr.Chatbot(elem_id="chatbot")
    user_input = gr.Textbox(
        show_label=False,
        placeholder="请输入一句话...",
        lines=2,
        container=False
    )

    gr.Examples(
        examples=[
            "你怎么还不回我？",
            "你是不是不想理我了？",
            "我只是说句玩笑话……"
        ],
        inputs=[user_input]
    )

    with gr.Row():
        submit_btn = gr.Button("发送", variant="primary")
        clear_btn = gr.Button("清空对话")

    history = gr.State([])
    past_key_values = gr.State(None)

    submit_btn.click(predict, [user_input, chatbot, history, past_key_values],
                     [chatbot, history, past_key_values])
    submit_btn.click(reset_user_input, [], [user_input])
    clear_btn.click(reset_state, outputs=[chatbot, history, past_key_values])

demo.queue().launch(share=True)
