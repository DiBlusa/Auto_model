import pyautogui
import keyboard
import time



# 4 segundos para abrir o navegador
time.sleep(4)
# Pressione a tecla "Esc" 3 vezes para encerrar o código.
esc_count = 0
while esc_count < 3:
    
    if keyboard.is_pressed('esc'):
        esc_count += 1
        print(f"\n[!] Tecla 'Esc' pressionada {esc_count} vezes.")
        # Aguarda a tecla ser solta para não contar múltiplas vezes
        while keyboard.is_pressed('esc'):
            time.sleep(0.1)

    # Selecionando o Texto UC Destino
    pyautogui.click(x=900, y=240)
    pyautogui.click(x=900, y=240)
    
    # Copiando texto 
    pyautogui.hotkey('ctrl', 'c')

    #Selecionando o Input UC Destino
    pyautogui.click(x=800, y=410)
    
    # Colando texto
    pyautogui.hotkey('ctrl', 'v')
    
     # Selecionando o Texto UC Destino
    pyautogui.click(x=900, y=310)
    pyautogui.click(x=900, y=310)
    
    # Copiando texto 
    pyautogui.hotkey('ctrl', 'c')

    #Selecionando o Input UC Destino
    pyautogui.click(x=800, y=475)
    
    # Colando texto
    pyautogui.hotkey('ctrl', 'v')

    # finalizando clickando "OK"
    pyautogui.click(x=790, y=520)

