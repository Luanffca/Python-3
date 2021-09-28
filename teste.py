# import os

# #cwd = os.getcwd()
# #pid = os.getpid()

# #print(cwd)
# #print(pid)

# print( os.environ['HOME'] )
# #print( os.environ['USER'] )
# #print( os.environ['USER'] )

# # d = os.getcwd()
# # f = 'logotipo.jpg'
# # print( os.path.join( d, 'dados', 'imagens', f ) )

from os import path, walk, chdir, getcwd, listdir

#caminho = 'C:\Users\luan\Documents\Eriana'
caminho = input('Digite o caminho: ')

chdir(caminho)
print(getcwd())

def recursive_walk(caminho):

    lista = []

    for raiz, subdirs, arquivos in walk(caminho):
        for f in arquivos:
            arquivo = path.join(raiz, f)
            lista.append(dict(tamanho=path.getsize(arquivo)))

        for subdir in subdirs:
            lista += recursive_walk(subdir)


    return lista

lista = recursive_walk(caminho)

print(lista,'\n')