
from os import chdir, getcwd, listdir
import os
caminho = input('Digite o caminho: ')

chdir(caminho)
print(getcwd())

# for c in listdir():
#     print(c)

lista = [f for f in os.listdir(caminho)]
tamanhos = []
dict_arquivos = {}

for item in lista:
    dict_arquivos[item] = os.path.getsize(caminho+item)

print(dict_arquivos)