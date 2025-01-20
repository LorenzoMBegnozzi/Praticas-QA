import os
import pyautogui
import time

imagem_botao_baixar = 'baixar.png'

def localizar_botao_baixar(imagem_botao_baixar, confidence=0.8):
    print(f"Procurando o botão de baixar com confiança {confidence}")
    posicao_botao = pyautogui.locateCenterOnScreen(imagem_botao_baixar, confidence=confidence)
    print(f"Posição do botão: {posicao_botao}")
    if posicao_botao is None:
        print("Botão não encontrado na tela.")
        return None
    return posicao_botao

def abrir_url(url):
    print(f"Abrindo a URL: {url}")
    
    # Abrindo o navegador
    pyautogui.press('win')
    pyautogui.write('opera') 
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=403, y=63)
    pyautogui.press('enter')
    
    time.sleep(5)  

    buscar_botao = localizar_botao_baixar(imagem_botao_baixar)
    if buscar_botao is None:
        print("Botão de baixar não encontrado.")
        return
    
    # Continuar o fluxo após encontrar o botão
    pyautogui.click(buscar_botao)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('qBitorrent')
    pyautogui.press('enter')

def abrir_menu():
    print("""
    #######################
    #                     #
    #   Escolha o filme   #
    #                     #
    #######################
    """)
    print("1 - Transformers 1 - 2007")
    print('2 - Transformers: A Vingança dos Derrotados')
    print('3 - Transformers: O Lado Oculto da Lua')
    print('4 - Transformers: A Era da Extinção')
    print('5 - Transformers: O Último Cavaleiro')
    print('6 - Transformers: O Despertar das Feras')
    print('0 - Sair')
    return input("Digite a opção desejada: ")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

FILMES_URL = {
    '1': 'https://limontorrents.com/transformers/',
    '2': 'https://limontorrents.com/transformers-a-vinganca-dos-derrotados/',
    '3': 'https://limontorrents.com/transformers-o-lado-oculto-da-lua/',
    '4': 'https://limontorrents.com/transformers-a-era-da-extincao/',
    '5': 'https://limontorrents.com/transformers-o-ultimo-cavaleiro/',
    '6': 'https://limontorrents.com/transformers-o-despertar-das-feras/',
}

def main():
    while True:
        opcao = abrir_menu()
        if opcao == '0':
            print("Saindo do programa...")
            break
        elif opcao in FILMES_URL:
            print(f"Abrindo o filme escolhido: {opcao}")
            abrir_url(FILMES_URL[opcao])
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
