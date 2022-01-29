import os

path = 'C:\\Users\\Pedrin\\Desktop\\Pedrin\\PYTHON\BOT DISCORD\\src\\champion\\'

for file in os.listdir(path):
    champ_list = file.split('.')
    champ = champ_list.pop(0)
    print(champ)
    with open('champions.txt', 'a') as champions:
        champions.write(champ+'\n')
        champions.close()
