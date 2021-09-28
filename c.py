from os import chdir, getcwd, listdir
import os
import json

file = open('lista.json', "w", encoding='utf8') 

caminho = input('Digite o caminho: ')

chdir(caminho)
print(getcwd())

for c in listdir():
    # print(c)
    # print(os.path.getsize(c))
    #json.dump('\\n', file)
    json.dump(c, file, indent=4)
    json.dump(os.path.getsize(c), file)

file.close()


# Gravar o arqruivo JSON
