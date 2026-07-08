# 🎵 Juice WRLD – "Hurt Me" (Karaoke ASCII Art)

A Python terminal script that pays tribute to Juice WRLD by combining **custom 999 ASCII art** with a **word‑by‑word karaoke player** for the song *"Hurt Me"*.  
The lyrics appear with rhythmic, variable pacing to match the flow of the verse.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)

---

## 📖 Overview

When you run the script:

1. A large **SKULL 999 ASCII** art appears in red.
2. You see the song title.
3. You press **ENTER** to start the verse (perfect for syncing with the actual song).
4. Every word is printed one after another, with delays that adjust to the length of each word and punctuation, mimicking the natural rhythm of Juice’s delivery.
5. Each line ends with a slightly longer pause, just like a bar in the track.
6. A final `🖤 999 forever.` closes the show.

---

## ✨ Features

- **🔥 Custom ASCII Art** – A bold red skull with the iconic "999" vibe.
- **🎤 Rhythmic Word‑by‑Word Printing** – Words appear with dynamic delays:
  - Longer words get slightly more time.
  - Punctuation (`, . ? !`) adds a tiny extra pause.
- **⏱️ Adjustable Speed** – Control the overall tempo with a single variable (`WPM_SPEED`).
- **🎨 Terminal Colors** – Bright red for the lyrics, dim gray for prompts.
- **⌨️ "Press ENTER" trigger** – Start the verse exactly when you want (great for karaoke nights).
- **🧹 Clean UI** – The "Press ENTER" prompt disappears automatically after you press it.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.6+** installed on your system.
- A terminal/console that supports **ANSI escape codes** (most modern terminals do – Command Prompt on Windows 10/11 works if you enable VT mode, which `os.system("")` tries to activate).

### Installation
1. Copy the full Python script into a file, e.g., `hurt_me.py`.
2. No external libraries are required – only the Python standard library (`time`, `sys`, `os`).

### Running the Script
```bash
python hurt_me.py

---

🖤 Credits
Artist: Juice WRLD (1998–2019) – 999 forever.

Song: "Hurt Me"

Script: Built with ❤️ by a fan, for the fans.

📜 License
This project is for personal and educational use only. All lyrics and artistic references belong to their respective owners.