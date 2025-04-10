# 👻 Ghost Shell

**Ghost Shell** is a beginner-friendly Python-based backdoor generator that automates payload creation for Windows, Linux, and Android using **msfvenom**. It also generates a ready-to-use Metasploit listener configuration — everything in one smooth workflow.

---

### 🚀 Features:
- One-click payload generation for Windows, Android, and Linux
- Auto listener setup with custom IP and port
- Animated loaders and themed UI (Matrix style intro 💻)
- Fully compatible with **Ngrok**, **Portmap.io**, and others
- Lightweight and easy to use, even for complete beginners
- Created by a **15-year-old** cybersecurity enthusiast 🤖

---

### 📌 Important Notes:
- This tool is for **educational use only**.
- It currently does **not** bypass antivirus or firewall.
- This is a **beginner-friendly** tool, not meant for advanced red teaming (yet).
- Upcoming features might include:
  - Antivirus evasion
  - Memory injection
  - Keyloggers
  - DNS spoofing
  - Phishing kits

---

### 💻 Supported Platforms:
- Kali Linux / Parrot OS ✅
- Debian / Ubuntu ✅
- Termux ✅
- Windows (WSL recommended) ✅

---

### ⚙️ Requirements:
- Python 3.x
- Metasploit Framework (includes msfvenom)

---

### 🛠️ Installation

#### Clone the Repository:
```bash
git clone https://github.com/yourusername/ghost-shell
cd ghost-shell
```

#### Debian / Ubuntu:
```bash
sudo apt update && sudo apt install python3 metasploit-framework -y
```

#### Termux:
```bash
pkg update && pkg install python metasploit -y
```

#### Windows via WSL:
```bash
sudo apt update && sudo apt install python3 metasploit-framework -y
```

#### Kali / Parrot OS:
✅ Already comes with Python and Metasploit pre-installed. You're good to go!

---

### ▶️ How to Use

1. Run the tool:
   ```bash
   python3 ghost-shell.py
   ```

2. Choose the type of backdoor you want to generate:
   - Windows `.exe`
   - Android `.apk`
   - Linux `.elf`

3. Enter your **LHOST** (IP address) and **LPORT** (port number) when prompted.

4. Ghost Shell will:
   - Create the payload using `msfvenom`
   - Animate the loading process
   - Auto-generate the correct Metasploit listener for you

5. After the payload is created, you’ll find it in your current directory.  
   ✅ Send it to your target and start the listener using the generated config.

---

### 📘 Example:
```bash
[*] Choose Platform:
1. Windows
2. Android
3. Linux

Input: 1
LHOST: 0.tcp.ngrok.io
LPORT: 12345
File Name: update.exe
```

---

### 🔒 Disclaimer:
> Ghost Shell is designed for **ethical hacking education only**.  
> The creator is **not responsible** for any misuse, illegal activity, or unauthorized access attempts.

---

### 💡 Why Use Ghost Shell?

Even if you already know how to make a backdoor manually, Ghost Shell automates everything in a sleek, themed interface with 1-click simplicity.  
Perfect for:
- Students and beginners learning cybersecurity
- Pentesters who want fast payload creation
- Hackers who love cool tools with visual vibes 😎

---

Made with 💀 by **UnixTail** (15 y/o cybersecurity enthusiast)  
Let’s make hacking beautiful and ethical 🔒
