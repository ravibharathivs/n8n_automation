import pyautogui
import time
import os

# ===== CONFIG =====
file_name = "pyauto.txt"
file_path = os.path.abspath(file_name)
file_exists = os.path.exists(file_path)

# ===== USER INPUT =====
user_input = input("Enter text to write: ")

# ===== OPEN FILE USING RUN (RELIABLE METHOD) =====
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Open file in Notepad (creates if not exists on save)
pyautogui.write(f'notepad "{file_path}"')
time.sleep(1)
pyautogui.press('enter')

# Wait for Notepad to open
time.sleep(2)

# ===== MOVE CURSOR TO END (FOR APPEND) =====
pyautogui.hotkey('ctrl', 'end')
time.sleep(0.5)

# If file already has content, add new line
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    pyautogui.press('enter')

# ===== WRITE TEXT =====
pyautogui.write(user_input, interval=0.05)

# ===== SAVE =====
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

# ===== HANDLE FIRST SAVE (NEW FILE ONLY) =====
if not file_exists:
    pyautogui.write(file_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

# ===== CLOSE =====
pyautogui.hotkey('alt', 'f4')
time.sleep(1)

print("✅ Done! Data appended correctly.")