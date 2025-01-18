import os
import time
import tkinter as tk
from tkinter import filedialog
import webbrowser
import pexpect
import keyboard
import pyautogui

def abrir_menu():
    print("""
    #######################
    #                     #
    # Escolha o framework #
    #     Para inciar     #
    #                     #
    #######################
    """)
    
    print("1 - Playwright")
    print("2 - Node.js + Express")
    print("3 - Pesquisar no youtube")
    print("4 - Pesquisar no chatGPT")
    print("5 - Entrar no Visual Studio Code")
    print("6 - Sair do programa")
    option = input("Digite a opção desejada: ")
    return option
##======================Playwright================
def selecionar_pasta():
    root = tk.Tk()
    root.withdraw() 
    caminho_play = filedialog.askdirectory(title="Selecione a pasta onde quer configurar o Playwright")    
    if caminho_play:
        print(f"Pasta selecionada: {caminho_play}")
        os.chdir(caminho_play)
        print(f"Pasta alterada para: {os.getcwd()}")
        configurar_playwright(caminho_play)
    else:
        print("Nenhuma pasta foi selecionada.")

def configurar_playwright(caminho_play):
    print("Configurando Playwright...")
    child = pexpect.spawn("npm init playwright@latest") 
    child.expect('Press Enter to continue:')
    child.sendline('') 
    child.expect('Do you want to install Playwright? (y/n):')
    child.sendline('y')
    child.expect(pexpect.EOF)  
    print("Configuração do Playwright concluída!")
    print("Entrando no projeto!!!")
    # Abre o projeto no VSCode
    os.system("code .")

##==========================Node===============================
def selecionar_pasta_node():
    root = tk.Tk()
    root.withdraw()
    caminho_node = filedialog.askdirectory(title="Selecione a pasta onde quer configurar o Node.js + Express")
    if caminho_node:
        print(f"Pasta selecionada: {caminho_node}")
        os.chdir(caminho_node)
        print(f"Pasta alterada para {os.getcwd()}")
        configurar_pasta_node(caminho_node) 
    else: 
        print("Nenhuma pasta selecionada")  
    
def configurar_pasta_node(caminho_node):
    print("Configurando Node.Js + Express")
    os.system("npm init -y")
    os.system("npm install express")
    print("Instalando o Nodemon para recarregar automaticamente o servidor")
    os.system("npm install --save-dev nodemon")
    
##========================Pesquisar no youtube============
def pesquisa_youtube():
    search_query = input("Digite o que você quer pesquisar no YouTube: ")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    time.sleep(3)

##================Pesquisar no chat
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
            selecionar_pasta()
        elif option =='2':
            selecionar_pasta_node()
        elif option == '3':
            pesquisa_youtube()
        elif option == '4':
            pesquisa_chat()
        elif option == '5':
            abrir_code()
        elif option == '6': 
            print("Saindo do programa")
            break 
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()