import pyautogui
import time

def localizar_botao_play(imagem_play, confidence=0.8):
    try:
        posicao_play = pyautogui.locateCenterOnScreen(imagem_play, confidence=confidence)
        if posicao_play is None:
            print("Botão não encontrado na tela.")
            return None
        print(f"Posição do botão encontrada: {posicao_play}")
        return posicao_play
    except Exception as e:
        print(f"Erro ao localizar botão: {e}")
        return None

def pesquisar_musica(nome_musica):
    try:
        pyautogui.press('win')
        pyautogui.write('spotify')
        pyautogui.press('enter')
        time.sleep(1) 
        pyautogui.hotkey('win', 'up') 
        pyautogui.hotkey('ctrl', 'k')  
        pyautogui.write(nome_musica)
        pyautogui.press('enter')
        print(f"Pesquisando por: {nome_musica}")
    except Exception as e:
        print(f"Erro ao pesquisar música: {e}")

def menu():
    print("""
    ########################
    #                      #
    # O que deseja escutar? #
    #                      #
    ########################
    """)
    print('1 - ACDC')
    print('2 - Tyler, The Creator')
    print('0 - Sair')
    return input("Digite a opção desejada: ")

def main():
    opcoes = {
        '1': "ACDC",
        '2': "Tyler, The Creator"
    }

    while True: 
        opcao = menu()
        if opcao in opcoes:
            pesquisar_musica(opcoes[opcao])
        elif opcao == '0':
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
