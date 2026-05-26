<img src="https://img.shields.io/badge/Python-Telegram%20Bot-blue?style=for-the-badge&logo=telegram&logoColor=white"/>

# 🤖 Telegram Bot Project

A Python-based Telegram bot built using **python-telegram-bot (async)** and **aiohttp**.  
This bot is designed to handle messages and respond efficiently using modern async architecture.

---

## ⚡ Features

- 🤖 Telegram message handling (async)
- ⚡ Fast response using `aiohttp`
- 🧠 Modular bot structure
- 🔄 Easy to expand with new commands
- 📡 Real-time message processing

---

## 🛠️ Technologies Used

![Python](https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg)
![Git](https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg)
![VS Code](https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg)

- 🐍 Python
- 📦 python-telegram-bot
- 🌐 aiohttp
- 🧪 Thonny / VS Code
- 🔧 Git & GitHub

---

## 📦 Libraries Used

```python id="lib1"
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
