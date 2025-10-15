import pyautogui
import time
import pyperclip

pyautogui.hotkey ('win','r')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)

pyperclip.copy('https://www.youtube.com/')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(0.10)

pyautogui.click (400, 150 )

pyperclip.copy('Senac')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')