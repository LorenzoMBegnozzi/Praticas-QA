import keyboard  # type: ignore
import pyautogui
import time

def abrir_menu():
    print("1 - Mandar mensagem")
    option = input("Digite a opção desejada: ")
    return option

def mensagem():
    textomensagem= input("informe oq deseja mandar: ")
    keyboard.press_and_release('win')
    time.sleep(1) 
    pyautogui.write('bloco de notas')
    pyautogui.press('enter')
    time.sleep(2) 
  
    for _ in range(99):
        pyautogui.write(f"{textomensagem}\n") 

def main():
    while True:
        option = abrir_menu()
        if option == '1':
            mensagem()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if _name_ == '_main_':
    main()