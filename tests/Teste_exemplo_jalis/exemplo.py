import pyautogui
import time

time.sleep(2) 
#ao encontrar o botao3.png, ele clica e depois verifica se o botao2.png apareceu para então clicar, 
def click_until_next_appears(current_button, next_button, confidence=0.6, interval=0.5):
    location = pyautogui.locateCenterOnScreen(current_button, confidence=confidence)
    if location:
        pyautogui.click(location)
        print(f"{current_button} clicado!")

        # Agora, procurar pelo botao2
        while not pyautogui.locateOnScreen(next_button, confidence=confidence):
            time.sleep(interval)
        
        # Quando o botao2 aparecer, clicar nele
        pyautogui.click(pyautogui.locateCenterOnScreen(next_button, confidence=confidence))
        print(f"{next_button} encontrado e clicado!")

# Exemplo de uso
click_until_next_appears('botao3.png', 'botao2.png')


#primeiro localiza o botao, e depois clica
while not pyautogui.locateOnScreen('botao1.png', confidence=0.8):
    time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen('botao1.png', confidence=0.8))

time.sleep(2)

while not pyautogui.locateOnScreen('botao3.png', confidence=0.8):
    time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen('botao3.png', confidence=0.8))

time.sleep(2)

while not pyautogui.locateOnScreen('botao2.png', confidence=0.8):
    time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen('botao2.png', confidence=0.8))

