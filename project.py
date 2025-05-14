import webbrowser
import time
import pyautogui

# Open WhatsApp Web
webbrowser.open("https://web.whatsapp.com/")
time.sleep(15)  # Wait for WhatsApp Web to load, adjust if needed

# Click on search bar - you may need to get exact coordinates with pyautogui.position()
# Example: Click top-left where the search bar is
pyautogui.click(x=219, y=260)
time.sleep(1)

# Type the contact name
pyautogui.write("Ritu", interval=0.1)
time.sleep(1)

# Press enter to open the chat
pyautogui.press("enter")

# Select chat and copy
import pyperclip

# Wait for you to manually open the chat or automate before this
time.sleep(2)

pyautogui.click(x=1848, y=868)

# Step 1: Move to the start of the number (adjust coordinates for your screen)
pyautogui.moveTo(919, 236)  # Replace with position near "919236"
pyautogui.mouseDown()
time.sleep(0.5)

# Step 2: Drag to end of number (adjust to end of "919893")
pyautogui.moveTo(903, 994)  # Drag to the right
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selection
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1884, 881)
time.sleep(0.5)

# Step 4: Get copied text
copied_text = pyperclip.paste()

from openai import OpenAI

client = OpenAI("Your API Key")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "You are person name Mehul from India and speaks Gujrati and English. Ritu is Mehul's wife. You analyze chat History and respond the conversation of Ritu as You are Mehul"},
               {"role": "user", "content": copied_text }
  ]
)

# AI=completion.choices[0].message
output= f"content='{completion.choices[0].message.content}'"

AI = output.split(":", 2)[-1].strip().rstrip("'")


pyperclip.copy(AI)
time.sleep(5)
pyautogui.click(x=1332, y=956)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
