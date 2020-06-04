# AULA 10 CONDIÇÕES SIMPLES E COMPOSTO PARTE 1
# Desafio 027
'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 peça para 
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

nume = int(input("Informe um número de 1 a 5. "))

num = randint(1, 5)
print("PROCESSANDO...")
sleep(3)
if nume == num:
    print("Você venceu!!!")
else:
    print("Você perdeu!!!")
print(num)
