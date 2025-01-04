from timeit import main
import keyboard
import pyautogui
import time
import webbrowser
import os

def abrir_menu():
    print("===QUAL PROJETO VC GOSTARIA DE INICIAR?===")
    print("1 - PyAutoGUI - Para automação de interface gráfica ")
    print("2 - Selenium - Para automação de browsers")
    print("3 - Playwright - Para automação de navegadores")
    print("4 - sair")
    option = input("Informe o número do projeto:)")
    return option

def criar_pasta():
    pyautogui.write('cd Documents', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3) 
    pyautogui.write('mkdir Pasta-Projeto && cd Pasta-Projeto')
    pyautogui.press('enter')
    time.sleep(3) 
    pyautogui.write('npm init -y')
    pyautogui.press('enter')
    time.sleep(3) 
    pyautogui.write('npm install playwright')
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.write('code .')
    pyautogui.press('enter')

def select_Playwright():
    keyboard.press_and_release('win')
    time.sleep(3)
    pyautogui.write('Bash')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=448, y=299)
    criar_pasta()

def main():
    while True: 
        option = abrir_menu()
        if option == '1':
            select_Playwright()
        elif option == '4': 
            print("Saindo do programa")
            break 
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
