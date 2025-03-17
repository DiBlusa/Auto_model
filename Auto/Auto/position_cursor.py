import pyautogui
import time

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException = True

try:
    while True:
        x, y = pyautogui.position()
        print(f'X: {x}, Y: {y}', end='\r')  # Atualiza a posição na mesma linha
        time.sleep(0.1)  # Atualiza a cada 0.1 segundos
except KeyboardInterrupt:
    print('\nParado pelo usuário.')

