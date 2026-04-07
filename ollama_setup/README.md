# Ollama Local LLM Setup & Response Writer

This guide walks you through installing Ollama, setting up a local LLM, and using the `ollama_input.py` script to get LLM responses and write them to a file.

---

## Table of Contents
1. [What is Ollama?](#what-is-ollama)
2. [Installation](#installation)
   - [Windows](#windows)
   - [macOS](#macos)
   - [Linux](#linux)
3. [Configuration](#configuration)
4. [Running Ollama Locally](#running-ollama-locally)
5. [Using the Script](#using-the-script)
6. [Troubleshooting](#troubleshooting)

---

## What is Ollama?

Ollama is a framework that lets you run large language models (LLMs) locally on your machine without needing cloud services. It provides a simple HTTP API to interact with models like Llama 2, DeepSeek, and others.

---

## Installation

### Windows

#### Step 1: Download Ollama
1. Visit the official website: [https://ollama.com](https://ollama.com)
2. Click the **"Download"** button
3. Select the **Windows** installer
4. The file will be named something like `OllamaSetup.exe`

#### Step 2: Install Ollama
1. Double-click the downloaded `OllamaSetup.exe` file
2. Follow the installation wizard:
   - Accept the license agreement
   - Choose installation directory (default is fine: `C:\Users\<YourUsername>\AppData\Local\Programs\Ollama`)
   - Click **Install**
3. Wait for the installation to complete
4. The installer will automatically start Ollama after installation

#### Step 3: Verify Installation
1. Open **Command Prompt** or **PowerShell**
2. Run the following command:
   ```cmd
   ollama --version
   ```
3. You should see the version number displayed

#### Step 4: Check Ollama Service
1. Ollama runs as a background service on Windows
2. Verify it's running by opening **Task Manager** (Ctrl+Shift+Esc)
3. Look for **Ollama** in the process list
4. If not running, restart your computer or run:
   ```cmd
   ollama serve
   ```

---

### macOS

#### Step 1: Download Ollama
1. Visit [https://ollama.com](https://ollama.com)
2. Click **Download**
3. Select **macOS** (Intel or Apple Silicon, depending on your Mac)
4. Save the `.dmg` file

#### Step 2: Install Ollama
1. Double-click the downloaded `.dmg` file
2. Drag the **Ollama** icon to the **Applications** folder
3. Wait for the copy process to complete
4. Eject the disc image

#### Step 3: Launch Ollama
1. Open **Finder**
2. Go to **Applications**
3. Double-click **Ollama**
4. Ollama will start and run in the background
5. You'll see the Ollama icon in the menu bar (top-right corner)

#### Step 4: Verify Installation
1. Open **Terminal** (Cmd+Space, type "Terminal", press Enter)
2. Run:
   ```bash
   ollama --version
   ```
3. You should see the version number

---

### Linux

#### Step 1: Download & Install (Automatic Script)
1. Open **Terminal**
2. Run the official installation script:
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```
3. Wait for the installation to complete

#### Step 2: Start Ollama Service
1. Start the Ollama service:
   ```bash
   ollama serve
   ```
2. Leave this terminal window open (Ollama runs in the foreground)
3. You should see output like:
   ```
   2024/04/07 10:30:45 Listening on 127.0.0.1:11434
   ```

#### Step 3: Verify Installation (In Another Terminal)
1. Open a **new Terminal** window
2. Run:
   ```bash
   ollama --version
   ```
3. You should see the version number

---

## Configuration

### Step 1: Download a Model

After installation, you need to download an LLM model. We'll use **DeepSeek R1 8B** (recommended for most systems).

#### On Windows (Command Prompt or PowerShell):
```cmd
ollama pull deepseek-r1:8b
```

#### On macOS or Linux (Terminal):
```bash
ollama pull deepseek-r1:8b
```

**Note:** This will download approximately 4.8 GB. It may take several minutes depending on your internet speed.

### Step 2: Verify Model Installation

Run:
```bash
ollama list
```

You should see output like:
```
NAME                    ID              SIZE      MODIFIED
deepseek-r1:8b         abc123def456    4.8 GB    1 minute ago
```

### Step 3: Alternative Models

If you want a smaller or different model, here are popular options:

- **Mistral** (7.3 GB): `ollama pull mistral`
- **Llama 2** (3.8 GB): `ollama pull llama2`
- **Neural Chat** (4.1 GB): `ollama pull neural-chat`
- **Phi** (1.6 GB - smallest): `ollama pull phi`

---

## Running Ollama Locally

### Start Ollama Server

Ollama runs as a HTTP server on your local machine at `http://127.0.0.1:11434`

#### Windows:
1. Ollama starts automatically on system startup
2. To manually start, open Command Prompt and run:
   ```cmd
   ollama serve
   ```

#### macOS:
1. Ollama starts automatically when you launch the app
2. Check the menu bar (top-right) for the Ollama icon
3. To manually start:
   ```bash
   ollama serve
   ```

#### Linux:
1. Open Terminal and run:
   ```bash
   ollama serve
   ```
2. Keep this terminal window open while using Ollama

### Verify Server is Running

Open a **new terminal/command prompt** and run:

```bash
curl http://127.0.0.1:11434/api/tags
```

You should see a JSON response showing available models.

---

## Using the Script

### Prerequisites

1. **Python 3.11+** installed
2. **Ollama running** locally (see above)
3. **Virtual environment** created and activated (optional but recommended)

### Step 1: Navigate to Project Directory

```bash
cd d:\Career\automation
```

Or on macOS/Linux:
```bash
cd ~/path/to/your/project
```

### Step 2: Activate Virtual Environment (If Using One)

#### Windows:
```cmd
myenv\Scripts\activate
```

#### macOS/Linux:
```bash
source myenv/bin/activate
```

### Step 3: Run the Script

#### Windows:
```cmd
python ollama_input.py
```

Or with full path:
```cmd
d:\Career\automation\myenv\Scripts\python.exe ollama_input.py
```

#### macOS/Linux:
```bash
python3 ollama_input.py
```

### Step 4: Enter Your Prompt

The script will prompt you:
```
Enter a prompt for Ollama: 
```

Type your question or prompt and press **Enter**.

**Example:**
```
What are the benefits of machine learning?
```

### Step 5: Wait for Response

The script will:
1. Send your prompt to the local Ollama server
2. Wait for the LLM to generate a response
3. Display status: `Sending prompt to local Ollama model 'deepseek-r1:8b' at 127.0.0.1:11434...`
4. Once complete: `Response written to ollama_response.txt`

### Step 6: Check the Response File

Open `ollama_response.txt` in your project directory to see the LLM's response.

The response will be in **English** (the script automatically ensures this).

---

## Script File: `ollama_input.py`

### How It Works

```python
import json
import os
import urllib.error
import urllib.request

LOCAL_OLLAMA_HOST = "127.0.0.1"
LOCAL_OLLAMA_PORT = 11434
MODEL_NAME = "deepseek-r1:8b"
OUTPUT_FILE = "ollama_response.txt"
```

**Key Components:**

1. **User Input**: Prompts user for text input
2. **API Call**: Sends prompt to Ollama HTTP API at `http://127.0.0.1:11434/api/generate`
3. **Language Control**: Prepends "Answer in English only." to ensure English responses
4. **File Write**: Saves response to `ollama_response.txt`

### Configuration

You can customize the script by setting **environment variables**:

#### Windows (Command Prompt):
```cmd
set OLLAMA_MODEL=mistral
set OLLAMA_HOST=127.0.0.1
set OLLAMA_PORT=11434
python ollama_input.py
```

#### macOS/Linux (Terminal):
```bash
export OLLAMA_MODEL=llama2
export OLLAMA_HOST=127.0.0.1
export OLLAMA_PORT=11434
python3 ollama_input.py
```

---

## Workflow Summary

```
┌─────────────────────────────────────────────────────┐
│  1. Start Ollama Service                            │
│     - Windows: Runs automatically or run manually   │
│     - macOS: Launch Ollama app                      │
│     - Linux: Run `ollama serve`                     │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  2. Run Python Script                               │
│     python ollama_input.py                          │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  3. Enter Your Prompt                               │
│     "What is Python?"                               │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  4. Script Sends HTTP Request                       │
│     POST http://127.0.0.1:11434/api/generate        │
│     Body: {"model": "deepseek-r1:8b", ...}          │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  5. Ollama Processes Request                        │
│     - LLM generates response                        │
│     - Returns JSON response                         │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  6. Script Writes Response to File                  │
│     ollama_response.txt                             │
└─────────────────────────────────────────────────────┘
```

---

## Troubleshooting

### Issue: "Unable to connect to Ollama"

**Cause:** Ollama service is not running

**Solution:**

#### Windows:
1. Open Command Prompt
2. Run: `ollama serve`
3. Keep the window open

#### macOS:
1. Check menu bar for Ollama icon
2. If not there, open Applications → Ollama
3. Run in Terminal: `ollama serve`

#### Linux:
```bash
ollama serve
```

---

### Issue: "HTTP error 404"

**Cause:** Model is not installed or wrong endpoint

**Solution:**
```bash
ollama list
ollama pull deepseek-r1:8b
```

---

### Issue: Response is in Chinese or Other Language

**Cause:** Model default language setting

**Solution:** Already handled by the script. It adds "Answer in English only." to every prompt.

---

### Issue: Out of Memory Error

**Cause:** Model too large for system RAM

**Solution:** Use a smaller model:
```bash
ollama pull phi          # 1.6 GB (smallest)
ollama pull neural-chat  # 4.1 GB
```

Then update `MODEL_NAME` in the script:
```python
MODEL_NAME = "phi"
```

---

### Issue: Slow Response Time

**Cause:** Large model or system resources

**Solution:**
1. Close other applications
2. Use a smaller model
3. Wait for response (may take 1-2 minutes for large models)

---

## System Requirements

### Minimum:
- **RAM:** 8 GB
- **Storage:** 10 GB free space
- **CPU:** Any modern processor
- **OS:** Windows 7+, macOS 10.13+, Linux (any distribution)

### Recommended:
- **RAM:** 16 GB or more
- **Storage:** 20+ GB free space
- **GPU:** NVIDIA/AMD (optional, speeds up generation)

---

## Additional Resources

- **Official Ollama Website:** https://ollama.com
- **Model Library:** https://ollama.com/library
- **API Documentation:** https://github.com/ollama/ollama/blob/main/docs/api.md
- **GitHub:** https://github.com/ollama/ollama

---

## Quick Start Checklist

- [ ] Downloaded Ollama from https://ollama.com
- [ ] Installed Ollama on your system
- [ ] Ollama service is running (`ollama serve`)
- [ ] Downloaded a model (`ollama pull deepseek-r1:8b`)
- [ ] Verified model is installed (`ollama list`)
- [ ] Navigated to project directory
- [ ] Activated virtual environment (if using one)
- [ ] Ran the script (`python ollama_input.py`)
- [ ] Entered a test prompt
- [ ] Checked `ollama_response.txt` for response

---

**Happy prompting! 🚀**
