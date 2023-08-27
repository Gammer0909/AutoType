import pyautogui
import time

# Simple pyautogui wrapper functions

def type(text, interval=0.1):
    for char in text:
        pyautogui.press(char)
        time.sleep(interval)
    return True

def Goto(x, y):
    pyautogui.moveTo(x, y)
    return True

def Click(x, y):
    pyautogui.click(x, y)
    return True

def Bold():
    pyautogui.hotkey('command', 'b')
    return True

def Italic():
    pyautogui.hotkey('command', 'i')
    return True

def Underline():
    pyautogui.hotkey('command', 'u')
    return True

