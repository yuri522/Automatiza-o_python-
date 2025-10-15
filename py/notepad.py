import pyautogui
import time
import subprocess
import pyperclip

pyautogui.hotkey('win', 'm')

time.sleep(2)

pyautogui.hotkey ('Ctrl', 'Shift', 'N')

pyautogui.write('Minha Pasta', interval = 0.1) 

time.sleep(4)

pyautogui.doubleClick(x=266, y=943 )

time.sleep(2)

pyautogui.rightClick ( x= 529, y= 590)

time.sleep(4)

for _ in range(13):
    pyautogui.press('down')

pyautogui.press('enter')  

time.sleep(5)

for _ in range(14):
    pyautogui.press('down')

pyautogui.press('enter')  

pyautogui.write('Arquivo.txt', interval = 0.1) 

pyautogui.press('enter')

time.sleep(4)

pyautogui.write ('Acabei',interval=0.10)

pyautogui.hotkey('alt','f4') 