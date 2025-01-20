import pyautogui
import time

def login_amazon():
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
login_amazon()


