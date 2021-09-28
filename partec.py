import os

path = "C:\Users\luan\Downloads"
lista = [f for f in os.listdir(path)]
tamanhos = []
dict_arquivos = {}

for item in lista:
    dict_arquivos[item] = os.path.getsize(path+item)

print(dict_arquivos)

from os import chdir, getcwd, listdir, path
import os

caminho = input('Digite o caminho: ')
tamanhos = []
dict_arquivos = {}

chdir(caminho)
print(getcwd())


for c in listdir():
    for item in c:
        dict_arquivos[item] = os.path.getsize(path+item)
        print(c)
        print(dict_arquivos)