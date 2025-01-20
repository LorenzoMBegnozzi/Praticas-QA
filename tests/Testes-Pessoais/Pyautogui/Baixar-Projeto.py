import os
import subprocess
import time
import tkinter as tk
from tkinter import filedialog
import webbrowser
import keyboard
import pyautogui

def abrir_menu():
    print("""
    #######################
    #                     #
    # Escolha uma opção   #
    #                     #
    #######################
    """)
    
    print("1 - Pesquisar no youtube")
    print("2 - Pesquisar no chatGPT")
    print("3 - Entrar no Visual Studio Code")
    print("4 - Sair do programa")
    option = input("Digite a opção desejada: ")
    return option

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

if __name__ == "__main__":
    main()
