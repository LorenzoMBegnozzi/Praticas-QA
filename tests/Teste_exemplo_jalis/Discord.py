import pyautogui
import time

botao_entrar = 'entrar.png'
imagem_verificacao = 'imagem_verificacao.png' 

def localizar_botao_entrar(botao_entrar, confidence=0.8):
    posicao_botao = pyautogui.locateCenterOnScreen(botao_entrar, confidence=confidence)
    return posicao_botao

def esperar_imagem_aparecer(imagem, confidence=0.8):
    print("Aguardando a imagem aparecer...")
    while True:
        posicao = pyautogui.locateOnScreen(imagem, confidence=confidence)
        if posicao is not None:
            print("Imagem encontrada!")
            break
        time.sleep(1)  

def abrir_discord():
    pyautogui.press('win')
    pyautogui.write('discord')
    pyautogui.press('enter')
    time.sleep(2)

def login():
    pyautogui.write('lorenzobegnozzi@hotmail.com')
    pyautogui.press('tab')
    pyautogui.write('Lorenzo0911@')
    botao_discord = localizar_botao_entrar(botao_entrar)
    pyautogui.click(botao_discord)

def main():
    abrir_discord()
    time.sleep(10)
    esperar_imagem_aparecer(imagem_verificacao) 
    login()
main()
