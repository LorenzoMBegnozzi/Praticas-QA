import keyboard
import pyautogui
import time
import webbrowser

def abrir_menu():
    print("""
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
    █░░║║║╠─║─║─║║║║║╠─░░█
    █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
    """)
    print("1 - Pesquisar no YouTube")
    print("2 - Perguntar ao Chat")
    print("3 - Entrar no Visual Studio Code")
    print("4 - Sair do programa")
    option = input("Digite a opção desejada: ")
    return option

def pesquisa_youtube():
    search_query = input("Digite o que você quer pesquisar no YouTube: ")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    time.sleep(3)

def pesquisa_chat():
    pesquisa = input("Digite o que você quer pesquisar no chat: ")
    webbrowser.open("https://chat.openai.com/")
    time.sleep(3)
    pyautogui.write(pesquisa)
    time.sleep(2)
    pyautogui.press('enter')

def abrir_code():
    keyboard.press_and_release('win')
    time.sleep(1)
    pyautogui.write('Visual Studio Code')
    time.sleep(1)
    pyautogui.press('enter')

def main():
    while True: 
        option = abrir_menu()

        if option == '1':
            pesquisa_youtube()
        elif option == '2':
            pesquisa_chat()
        elif option == '3':
            abrir_code()
        elif option == '4': 
            print("Saindo do programa")
            break 
        else:
            print("Opção inválida.")

if _name_ == "_main_":
    main()