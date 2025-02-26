import pyautogui
import time

imagem_botao_baixar = 'baixar.png'

# Aguarde alguns segundos para abrir a tela e verificar o botão
time.sleep(5)

# Tenta localizar o botão na tela
posicao_botao = pyautogui.locateCenterOnScreen(imagem_botao_baixar, confidence=0.8)

if posicao_botao is not None:
    print(f"Botão encontrado na posição: {posicao_botao}")
else:
    print("Botão não encontrado. Verifique a captura da tela.")
