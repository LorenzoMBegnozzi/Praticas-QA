import pyautogui
import time

time.sleep(2)

def item_no_carrinho():
    pyautogui.click(x=943, y=136)
    pyautogui.write('Notebook Acer 2025')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=497, y=494)
    time.sleep(2)
    pyautogui.click(x=1530, y=492)
    time.sleep(5)
    pyautogui.click(x=1553, y=331)   
item_no_carrinho()