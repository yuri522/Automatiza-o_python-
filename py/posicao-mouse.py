import pyautogui
import time

print("Pressione Ctrl+C para Parar.")

while True:
    x, y = pyautogui.position()
    print(f"Posição atual do Mouse: X={x}, Y={y}")
    time.sleep(0.1)
