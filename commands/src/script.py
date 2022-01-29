import pyautogui as pa
from time import sleep

def wait():
    sleep(.5)

def pegar_runa(champ):
    # URL
    pa.moveTo(421, 51, .5)
    pa.click()
    wait()
    pa.write(f'https://www.leagueofgraphs.com/pt/champions/runes/{champ}')
    wait()
    pa.press('enter')
    sleep(2)

    # # SCROLL
    pa.moveTo(1360, 132)
    pa.dragTo(1360, 184, .2, button='left')

    # # HOTKEY PRINT
    pa.hotkey('win', 'shift', 's')
    wait()
    pa.moveTo(577,223)
    pa.mouseDown()
    pa.moveTo(810,745)
    pa.mouseUp()
    sleep(2)

    # ABRIR PRINT
    pa.click(1199,635)
    sleep(2)
    pa.click(700,84)

    # SALVAR
    sleep(1)
    pa.press('backspace')
    sleep(1)
    pa.write(champ, .1)
    sleep(2)
    pa.click(561, 472)
    pa.click(827, 48)







x =0

with open('champions.txt', 'r') as champions:
    for a in champions:
        pegar_runa(a.lower())
        x += 1
        print(x)
        if x == 157:
            break

