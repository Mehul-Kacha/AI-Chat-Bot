#First we have to calibrate our courser and find its positions for our program 
import pyautogui

while True:
    a = pyautogui.position()
    print(a)
