<h1 align='center'>🌸 DaiyuLM: Lin Daiyu-style Emotional Dialogue Model</h1>
<p align="center">
  <img src="assets/daiyu.png" alt="Daiyu" width="140"/>
</p>

<h3 align="center">
A dialogue generation model inspired by Lin Daiyu's poetic melancholy, fine-tuned from ChatGLM2-6B using Prefix-Tuning.
</h3>

<p align="center">
  <a href="README.md">简体中文</a> | <b>English</b>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/caixiaoshun/DaiyuLM">Live Demo</a> · 
  <a href="https://github.com/caixiaoshun/DaiyuLM">GitHub</a> · 
  <a href="mailto:cs.shunzhang@foxmail.com">Contact</a>
</p>

---

## 🌟 Highlights

- 🎭 Fine-tuned on 142 Lin-Daiyu-style Q&A pairs; excels at producing poetic, melancholic, and emotionally charged responses
- ⚙️ Based on ChatGLM2‑6B with **Prefix-Tuning**, achieving efficient training with minimal parameter overhead
- 💬 Supports streaming dialogue with a Gradio-powered interactive chatbot UI

---

## 📚 Dataset Overview

- Total of **142 Q&A samples**
  - 21 manually curated from forums and social media (Douban, Zhihu, etc.)
  - 121 generated and refined using **GPT‑4o** for stylistic consistency
- Topics focus on emotional expression, misunderstandings, and romantic frustration in a literary tone

---

## 🚀 Getting Started

### 1️⃣ Install dependencies

```bash
git clone https://github.com/caixiaoshun/DaiyuLM.git
cd DaiyuLM
pip install -r requirements.txt
````

### 2️⃣ Prepare the model

* Download [ChatGLM2‑6B](https://huggingface.co/THUDM/chatglm2-6b) weights and tokenizer
* Place `pytorch_model.bin` (Prefix-Tuning weights) into the project root

```bash
DaiyuLM/
├── app.py
├── requirements.txt
├── README.md
├── README_EN.md
└── checkpoint/
    └── pytorch_model.bin
```

### 3️⃣ Launch demo

```bash
python app.py
```

Then open the local Gradio interface in your browser to start chatting.

---

## 💬 Sample Dialogue

![lindaiyu](https://github.com/user-attachments/assets/2b4b5c0f-f9ff-4a94-a68e-7d2841c4ba65)

| Input                      | DaiyuLM Output                                                                     |
| -------------------------- | ---------------------------------------------------------------------------------- |
| `Why haven't you replied?` | `I fear I won’t last the day; just waiting for your reply has wearied me.`         |
| `Are you ignoring me?`     | `If you truly feel so, then perhaps silence suits us best... lest I appear petty.` |

---

## 🧠 Model Details

* **Base Model**: ChatGLM2-6B
* **Fine-tuning**: Prefix-Tuning (prefix length = 128)
* **Dialogue Style**: Literary, sorrowful, emotionally resonant
* **Optimization**: Efficient parameter tuning with low compute demand

---

## 🧰 Applications

* ✅ Deployable as CPU-friendly web demo
* 📦 Exportable to API for integration in other platforms
* 🎭 Extendable to other *Dream of the Red Chamber* characters (e.g., Baoyu, Xifeng)

---

## 🙋 FAQ

**Q: Do I need a GPU to run it?**
A: No. It works on CPU, but GPU is recommended for better speed.

**Q: Can I use quantized models (e.g., INT4)?**
A: Yes! ChatGLM2 supports quantization with `bitsandbytes` or pre-quantized weights.

---

## 📬 Contact & Contribution

💌 Email: [cs.shunzhang@foxmail.com](mailto:cs.shunzhang@foxmail.com)
💡 If you'd like to add more characters or deploy the model in new formats, feel free to submit an issue or contact the author.

---

## ✅ Support
If you enjoy this project, feel free to support the author with a cup of tea ☕:

<p align="center">
  <img src="assets/alipay.png" alt="支付宝" height="260"/>
</p>

## 📄 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

> 🙏 Powered by ChatGLM2 and inspired by the enduring sorrow of Lin Daiyu from *Dream of the Red Chamber*.

