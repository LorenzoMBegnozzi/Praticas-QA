import pyautogui
import time

pyautogui.PAUSE = 0.5

def login_amazon():
    """Realiza o login na Amazon."""
    pyautogui.press('win')
    pyautogui.write('opera')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    pyautogui.click(x=589, y=54)
    pyautogui.write('amazon.com.br')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(x=1610, y=131)
    time.sleep(1)
    pyautogui.click(x=1575, y=190)
    time.sleep(2)
    pyautogui.write('lorenzobegnozzi@hotmail.com')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('Lorenzo0911@')
    pyautogui.press('enter')
    time.sleep(3)

def item_no_carrinho():
    """Adiciona um item ao carrinho de compras."""
    pyautogui.click(x=943, y=136)  # Clica no campo de busca
    pyautogui.write('Notebook Acer 2025')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=497, y=494)  # Clica no item encontrado
    time.sleep(2)
    pyautogui.click(x=1530, y=492)  # Clica no botão de adicionar ao carrinho
    time.sleep(5)
    pyautogui.click(x=1546, y=334) # Clica no carrinho para visualizar
    time.sleep(2)

def removendo_do_carrinho():
    """Remove o item do carrinho de compras."""
    pyautogui.click(x=514, y=611)  # Clica no item no carrinho
    time.sleep(2)
    pyautogui.click(x=130, y=136)  # Clica para remover o item do carrinho


login_amazon()
item_no_carrinho()
removendo_do_carrinho()

