import pyautogui
import time 

pyautogui.hotkey ('win','r')
pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(2)

pyautogui.write('https://www.google.com/',interval= 0.2 )
pyautogui.press('enter')