WhatsApp Chat Auto-Responder Bot using GPT-4o

This Python script automates the process of reading messages from WhatsApp Web, analyzing them with OpenAI's GPT-4o model, and sending an intelligent response as if it were sent by a specific person.

Features

Automatically opens WhatsApp Web

Searches for a specific contact (Name)

Selects the latest chat message

Sends it to OpenAI's API with custom persona configuration

Copies AI-generated response and sends it back in the chat


Prerequisites

Python 3.x

Chrome or any default browser

Required Python libraries:
```
pip install pyautogui pyperclip openai

```
Setup

1. Replace "Your API Key" in the script with your actual OpenAI API key.


2. Adjust all pyautogui coordinates (x, y) based on your screen resolution using pyautogui.position() to capture positions manually.


3. Make sure your system allows clipboard access and automation.



How It Works

1. Opens WhatsApp Web.


2. Waits for the page to load and clicks the search bar.


3. Searches and opens the chat with Ritu.


4. Selects the latest message.


5. Sends the message to OpenAI with context (Mehul's persona).


6. Copies and sends the response back in WhatsApp.



Important Notes

This script uses screen coordinates which are resolution dependent. You must calibrate them for your system.

Make sure WhatsApp Web is logged in before running the script.

For safety, keep your API key private and secure.


License

This project is licensed under the MIT License.


---
