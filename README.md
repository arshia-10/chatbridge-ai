# 🤖 ChatBridge AI – Personal Inbox Agent

A privacy-first AI messaging assistant that reads your Telegram messages and replies in your tone — powered entirely by **local LLMs (Mistral via Ollama)**.

---

## 🌟 Overview

**ChatBridge AI** is designed to act like your personal communication assistant. It observes incoming Telegram messages, understands context, and generates human-like replies that match your communication style — all while keeping your data completely private.

Unlike cloud-based AI tools, ChatBridge runs **locally on your machine**, ensuring:

* 🔒 Zero data leakage
* ⚡ Faster responses (no API latency)
* 💸 No API costs

---

## 🚀 Features

* ✅ **Personalized Replies** – Responds in your tone and style
* ✅ **Local LLM Integration** – Uses Mistral via Ollama (no OpenAI or external APIs)
* ✅ **Privacy-First Architecture** – All data stays on your system
* ✅ **Real-time Telegram Bot** – Automatically reads and replies to messages
* ✅ **Async Python Backend** – Fast and scalable message handling
* ✅ **Extensible Design** – Easily add new features like summarization, scheduling, etc.

---

## 🧠 How It Works

1. Telegram bot receives a message
2. Message is passed to the local LLM (Mistral via Ollama)
3. LLM generates a context-aware response
4. Bot sends the reply back to Telegram

---

## 🏗️ Tech Stack

* **Backend:** Python (Asyncio, FastAPI/Telebot)
* **LLM:** Mistral (via Ollama)
* **Messaging API:** Telegram Bot API
* **Local Inference:** Ollama

---

## 📂 Project Structure

```
ChatBridge-AI/
│── bot/
│   ├── handlers.py
│   ├── bot.py
│
│── llm/
│   ├── mistral_client.py
│
│── utils/
│   ├── prompt_builder.py
│
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/chatbridge-ai.git
cd chatbridge-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama & Pull Mistral

```bash
ollama pull mistral
```

### 4️⃣ Set Up Telegram Bot

* Create a bot using **BotFather** on Telegram
* Copy your bot token

### 5️⃣ Configure Environment Variables

Create a `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_token_here
```

### 6️⃣ Run the Project

```bash
python main.py
```

---

## 🔐 Privacy & Security

* No external API calls
* No data storage outside your system
* Fully local inference using Ollama

---

## 💡 Future Enhancements

* ✨ Multi-platform support (WhatsApp, Email)
* ✨ Message summarization
* ✨ Smart auto-replies based on priority
* ✨ Voice-to-text integration
* ✨ Fine-tuned personal tone model

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Ollama for local LLM support
* Mistral AI for open-weight models
* Telegram Bot API

---

## 📬 Contact

For queries or collaboration:

* GitHub Issues
* LinkedIn (add your profile here)

---

⭐ If you like this project, consider giving it a star!
