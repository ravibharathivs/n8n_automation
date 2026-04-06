# PyAutoGUI Automation Script

## Overview
The `pyauto.py` script is a Python automation tool that uses the `pyautogui` library to automatically write user-provided text to a file using Windows Notepad. This demonstrates basic GUI automation for file operations.

## Functionality

### Core Features
- **Text Input**: Prompts the user to enter text to write to the file
- **File Management**: Works with a file named `pyauto.txt` in the current directory
- **Append Mode**: Automatically appends new text to existing content
- **GUI Automation**: Uses keyboard shortcuts and mouse simulation to control Notepad

### How It Works
1. **Configuration**: Sets up the target file path (`pyauto.txt`)
2. **User Input**: Collects text from the user via command line input
3. **File Opening**: Launches Notepad using Windows Run dialog (`Win + R`)
4. **Content Management**: 
   - Moves cursor to end of file for appending
   - Adds a new line if file already has content
5. **Text Writing**: Types the user input with a small delay between characters
6. **Save Operation**: Saves the file using `Ctrl + S`
7. **New File Handling**: For new files, provides the file path in the save dialog
8. **Cleanup**: Closes Notepad using `Alt + F4`

## Requirements
- Python 3.x
- `pyautogui` library (`pip install pyautogui`)
- Windows operating system (uses Notepad)

## Usage
```bash
python pyauto.py
```

When prompted, enter the text you want to append to the file.

## Limitations
- Windows-specific (uses Notepad)
- Requires GUI access (cannot run headless)
- May be affected by system focus changes
- Uses fixed timing delays (not event-driven)

## Safety Notes
- The script simulates keyboard input, so ensure no important windows are open
- Test in a safe environment first
- The automation may fail if system focus changes during execution

## Flask API Version

A Flask-based REST API version of the automation script has been created in `flask_pyauto.py`.

### API Endpoint
- **URL**: `/append_text`
- **Method**: POST
- **Content-Type**: application/json

### Request Payload
```json
{
  "text": "Your text to append here"
}
```

### Response
- **Success (200)**: `{"message": "Text appended successfully to pyauto.txt"}`
- **Error (400)**: `{"error": "Missing 'text' field in payload"}` or `{"error": "'text' must be a string"}`
- **Error (500)**: `{"error": "<exception message>"}`

### API Requirements
- Python 3.x
- `flask` library (`pip install flask`)
- `pyautogui` library (`pip install pyautogui`)
- Windows operating system

### Running the API
```bash
python flask_pyauto.py
```

The API will start on `http://127.0.0.1:5000/` by default.

### Usage Example
```bash
curl -X POST http://127.0.0.1:5000/append_text \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from API!"}'
```

## n8n Workflow Integration

An n8n workflow has been configured to automate content creation and integrate with the Flask API via ngrok tunneling. The workflow configuration is stored in `puautogui_ngrok_clud.json`.

### Workflow Overview
The n8n workflow creates an automated pipeline that:
1. **Scheduled Trigger**: Runs every 2 minutes
2. **Date/Time Fetching**: Gets current readable date and time
3. **AI Content Generation**: Uses OpenAI GPT model to create creative content for the timeline
4. **API Integration**: Sends generated content to the Flask API via ngrok tunnel

### Workflow Components

#### 1. Schedule Trigger
- **Node**: `Triggering schduler on every 2 minuts`
- **Type**: `n8n-nodes-base.scheduleTrigger`
- **Configuration**: Triggers every 1 minute (despite the name saying 2 minutes)
- **Purpose**: Initiates the automated workflow at regular intervals

#### 2. Date/Time Processing
- **Node**: `fetching current date and time`
- **Type**: `n8n-nodes-base.dateTime`
- **Configuration**: Outputs readable date format
- **Purpose**: Provides timestamp context for content generation

#### 3. AI Content Generation
- **Node**: `Basic LLM Chain`
- **Type**: `@n8n/n8n-nodes-langchain.chainLlm`
- **Model**: OpenAI GPT (configured as "gpt-5-mini")
- **Prompt**: Creates creative content for the timeline in one single line
- **Purpose**: Generates automated content using AI

#### 4. API Integration
- **Node**: `HTTP Request`
- **Type**: `n8n-nodes-base.httpRequest`
- **Method**: POST
- **URL**: `https://antagonistically-interastral-aden.ngrok-free.dev/append_text`
- **Payload**: Sends the generated text from the AI model
- **Purpose**: Delivers content to the Flask API for file appending

### n8n Setup Requirements
- n8n instance (self-hosted or cloud)
- OpenAI API credentials configured
- ngrok tunnel exposing the Flask API
- Import the workflow from `puautogui_ngrok_clud.json`

### ngrok Setup on Windows

ngrok creates a secure tunnel from your local Flask API to a public URL that n8n can access. Follow these steps to set up ngrok on Windows:

#### 1. Download ngrok
- Visit https://ngrok.com/download
- Download the Windows version (ngrok.exe)
- Extract the executable to a folder (e.g., `C:\ngrok\`)

#### 2. Sign up for ngrok Account
- Go to https://dashboard.ngrok.com/signup
- Create a free account
- Verify your email

#### 3. Authenticate ngrok
- Open Command Prompt or PowerShell
- Navigate to the folder containing ngrok.exe
- Run the authentication command:
  ```bash
  ngrok config add-authtoken YOUR_AUTH_TOKEN
  ```
  (Replace `YOUR_AUTH_TOKEN` with the token from your ngrok dashboard)

#### 4. Start the Flask API
- Ensure your Flask API (`flask_pyauto.py`) is running:
  ```bash
  python flask_pyauto.py
  ```
- Note the local URL (usually `http://127.0.0.1:5000`)

#### 5. Create ngrok Tunnel
- In a new Command Prompt/PowerShell window, run:
  ```bash
  ngrok http 5000
  ```
- ngrok will display a public URL (e.g., `https://abc123.ngrok-free.app`)
- Copy this URL for use in the n8n workflow

#### 6. Update n8n Workflow (Optional)
- If the ngrok URL changes, update the HTTP Request node in n8n:
  - Change the URL from `https://antagonistically-interastral-aden.ngrok-free.dev/append_text`
  - To your new ngrok URL: `https://your-new-url.ngrok-free.app/append_text`

#### 7. Test the Connection
- With both Flask API and ngrok running, test the endpoint:
  ```bash
  curl -X POST https://your-ngrok-url.ngrok-free.app/append_text \
    -H "Content-Type: application/json" \
    -d '{"text": "Test from ngrok"}'
  ```

#### ngrok Tips
- **Free Tier Limitations**: ngrok free tier URLs change on restart
- **Paid Tier**: Consider upgrading for static URLs
- **Security**: Keep your auth token secure
- **Monitoring**: Check ngrok dashboard for tunnel status and analytics

### Workflow Connections
- Scheduler → Date/Time → AI Chain → HTTP Request
- OpenAI Chat Model connected to Basic LLM Chain

### Notes
- The workflow is currently set to `active: false` in the JSON
- Uses ngrok for external access to the local Flask API
- Designed for continuous automated content generation and logging
