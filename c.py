from os import chdir, getcwd, listdir
import os

caminho = input('Digite o caminho: ')

chdir(caminho)
print(getcwd())

for c in listdir():
    print(c)
    print(os.path.getsize(c))