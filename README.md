<h1 align='center'>🌸 DaiyuLM：林黛玉式情绪对话模型</h1>
<p align="center">
  <img src="assets/daiyu.png" alt="Daiyu" width="140"/>
</p>

<h3 align="center">
基于 ChatGLM2-6B 的中文风格微调模型，擅长生成婉转、含蓄、略带怨气的“林黛玉式”发疯文学风格回复。
</h3>

<p align="center">
  <b>简体中文</b> | <a href="README_EN.md">English</a>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/caixiaoshun/DaiyuLM">在线体验</a> · 
  <a href="https://github.com/caixiaoshun/DaiyuLM">GitHub</a> · 
  <a href="mailto:cs.shunzhang@foxmail.com">联系作者</a>
</p>

---

## 🌟 特点亮点

- 🎭 微调于 142 条“林黛玉”风格对话，善于表达含蓄、情绪化、古典中文式委婉发疯
- ⚙️ 基于 ChatGLM2-6B，使用 Prefix-Tuning 技术，仅调整少量参数，部署效率高
- 💻 支持流式对话体验，Gradio 前端界面让交互更贴近真实

---

## 📚 数据来源说明

- 🔍 共计 142 条中文 QA 样本：
  - 其中 21 条精挑自豆瓣、知乎等平台的“林黛玉式发言”
  - 其余 121 条由 GPT‑4o 生成，并经人工筛选与润色，保证风格统一
- 数据围绕“发疯”、“误会”、“感情” 等情绪话题展开，强调主观怨气与表达含蓄

---

## 🚀 快速开始

### 1️⃣ 安装依赖

```bash
git clone https://github.com/caixiaoshun/DaiyuLM.git
cd DaiyuLM
pip install -r requirements.txt
````


### 2️⃣ 准备模型

* 下载 [ChatGLM2‑6B](https://huggingface.co/THUDM/chatglm2-6b) 原始模型及 tokenizer。
  最推荐的方式是使用 Hugging Face CLI 工具下载：

```bash
huggingface-cli download --resume-download THUDM/chatglm2-6b --local-dir checkpoint/chatglm2-6b
```

* 如果你在中国大陆下载较慢，可以设置国内镜像加速地址后再执行下载命令：

```bash
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --resume-download THUDM/chatglm2-6b --local-dir checkpoint/chatglm2-6b
```

* 下载完成后，将微调后的前缀参数放入 `checkpoint/` 目录中：

```bash
DaiyuLM/
├── app.py
├── requirements.txt
├── README.md
├── README_EN.md
└── checkpoint/
    ├── chatglm2-6b/                         # 下载的原始模型目录
    ├── pytorch_model.bin                   # 使用 21 条互联网数据训练的模型（epoch 未记录）
    └── pytorch_model_step_253000_141.bin   # 使用 142 条数据训练，253000 步保存
```

你可以通过以下命令启动 Gradio 应用：

```bash
python app.py --model_name_or_path checkpoint/chatglm2-6b --checkpoint checkpoint/pytorch_model_step_253000_141.bin
```

如果不指定参数，则默认使用 `checkpoint/pytorch_model.bin`。

---

## 💬 对话示例

![lindaiyu](https://github.com/user-attachments/assets/2b4b5c0f-f9ff-4a94-a68e-7d2841c4ba65)

| 用户输入       | 林黛玉回复                          |
| ---------- | ------------------------------ |
| 你怎么还不回我？   | 我大抵是熬不过这一天了，单单是等你的消息就心烦。       |
| 你是不是不想理我了？ | 哥哥要是这般态度，倒不如直接不理我的好，显得我无理取闹了些。 |
| 我只是说句玩笑话…  | 可惜我不是玩笑话中人。你一句轻描淡写，我却记在心头一整夜。  |

---

## 🧠 模型配置

* **基座模型**：ChatGLM2-6B
* **微调方式**：Prefix-Tuning（前缀长度为 128）
* **是否支持流式对话**：✅
* **参数总量变更**：约提升 0.1%（无须全量微调）

---

## 🔧 可扩展性建议

* 🔁 追加训练样本：支持更多“红楼梦”人物风格，如贾宝玉、王熙凤
* 🧪 支持 API 接口化部署：可集成至网页、微信小程序或 QQ Bot
* 🖥️ 支持 INT4 量化部署，适用于低资源环境

---

## 🙋 FAQ

**Q1：我可以不用 GPU 吗？**
A：可以。模型推理阶段可以在 CPU 上运行，但速度略慢。

**Q2：如何使用 INT4 加速？**
A：建议使用 `chatglm2-6b-int4` 模型版本，或结合 `bitsandbytes` 进行量化加载。

---

## 📬 联系方式

如需添加新风格或部署为 API，请联系作者或提交 Issue。

* 📮 邮箱：`cs.shunzhang@foxmail.com`
* 🧠 灵感源自：红楼梦中的林黛玉人物设定与现实网络发疯文学

---

## ✅ 支持作者
如果你喜欢这个项目，也欢迎请作者喝杯茶 ☕：

<p align="center">
  <img src="assets/alipay.png" alt="支付宝" height="260"/>
</p>

<p align="center"><em>扫码支持❤️</em></p>

---

## 📄 License

本项目遵循 [Apache 2.0 License](LICENSE)，欢迎商用、改进与再开发。

---

> 💡 **致谢**：感谢 THUDM 团队开源 ChatGLM2，同时也感谢林妹妹在中文文本生成世界中的灵魂启发。
