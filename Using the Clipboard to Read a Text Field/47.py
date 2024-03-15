#python3! - Note that the window functions of PyAutoGUI only work on Windows as of PyAutoGUI version 1.0.0, and not on macOS or Linux.

import pyautogui
import pyperclip

def click():
    try:
        pyautogui.click()
    except:
        pass

pyperclip.copy('text')
pyautogui.moveTo(4796, 714)
click()
pyperclip.paste()
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
