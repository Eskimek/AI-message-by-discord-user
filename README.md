[![Eskimai](https://github.com/Eskimek/AI-message-by-discord-user/blob/main/assets/logo2lightmode.png#gh-light-mode-only)](https://github.com/Eskimek/AI-message-by-discord-user)
[![Eskimai](https://github.com/Eskimek/AI-message-by-discord-user/blob/main/assets/logo1.png#gh-dark-mode-only)](https://github.com/Eskimek/AI-message-by-discord-user)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Edge WebDriver](https://img.shields.io/badge/Edge-WebDriver-0078D7?style=for-the-badge&logo=microsoft-edge)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium)](https://www.selenium.dev/)
[![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord)](https://discord.com/)

## 💡 About

**Eskimai Discord Bot** is a local automation script that combines Discord, Selenium and a local AI model (via Ollama) to auto-reply in DMs or private channels. Think of it as your own personal AI minion running on Microsoft Edge.

## 🚀 What It Does

1. Opens Discord in Microsoft Edge using your local profile.
2. Monitors the latest messages in a specific channel.
3. Sends the messages to your custom AI model (`eskimai`) via Ollama API. # You can change "eskimai" to your own model
4. Sends the AI’s response right back into Discord.

## ⚙️ Requirements

- Python 3.10+
- Microsoft Edge installed
- Edge WebDriver (handled by `webdriver-manager`)
- Ollama running locally with a model (`eskimai`)
- A local Discord login session in Edge

## 🛠 Installation

```bash
pip install selenium webdriver-manager requests
