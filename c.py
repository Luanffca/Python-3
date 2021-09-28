from os import chdir, getcwd, listdir

caminho = input('Digite o caminho: ')

chdir(caminho)
print(getcwd())

for c in listdir():
        print(c)