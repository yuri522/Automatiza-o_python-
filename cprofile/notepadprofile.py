import pyautogui
import time
import subprocess

def abrir_bloconotas():
    subprocess.Popen('notepad')
    time.sleep(1.5)

def escrever_texto():
    texto = "Ola, isso vai ser automatico" * 4
    pyautogui.write(texto, interval= 0.05)

def salvar_arquivo():
    pyautogui.hotkey('ctrl','s')
    time.sleep(1)
    pyautogui.write("arquivo.txt", interval=0.05)
    pyautogui.press('enter')

def fechar_bloconotas():
    time.sleep(1)
    pyautogui.hotkey('alt' ,'f4')

def automacao_completa():
    abrir_bloconotas()
    escrever_texto()
    salvar_arquivo()
    fechar_bloconotas()

if __name__ == "__main__":    
    import cProfile
    cProfile.run("automacao_completa()")  