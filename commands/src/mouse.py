import pyautogui
import os

while True:
    x,y = pyautogui.position()
    print('Posição atual do mouse')
    print(f'x: {x} y: {y}')
    os.system("cls")
