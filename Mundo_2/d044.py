# Desafio 044 
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Pedra', 'Tesoura' )
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PERAL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("kEN")
sleep(1)
print("PÔ")
sleep(1)
print("-=" * 15)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 15)
if computador == 0: #pedra
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGANDOR VENCEU!")
    elif jogador == 2: 
        print("COMPUTADOR VENCEU")
    else:
        ("JOGADA INVÁLIDA!")
elif computador == 1: #papel
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2: 
        ("JOGANDOR VENCEU!")
    else:
        ("JOGADA INVÁLIDA!")
elif computador == 2: # Tesoura
    if jogador == 0:
        ("JOGANDOR VENCEU!")
    elif jogador == 1:
        ("COMPUTADOR VENCEU")
    elif jogador == 2: 
        ("EMPATE!")
    else:
        ("JOGADA INVÁLIDA!")