import os
import tkinter as tk
from tkinter import filedialog

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
    print("2 -  teste ")
    print("3 - Sair do programa")
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
    os.system("npm init -y")
    os.system("npm install playwright")
    os.system("npx playwright install")
    print("Configuração do Playwright concluída!")
    print("Entrando no projeto!!!")
    os.system("code .")
    
      
def main():
    while True: 
        option = abrir_menu()

        if option == '1':
            selecionar_pasta()
        elif option =='2':
            selecionar_node()
        elif option == '3': 
            print("Saindo do programa")
            break 
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()