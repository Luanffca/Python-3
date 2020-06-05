# Desafio 037
'''Escreva um programa que leia dois número inteiro e compare-os mostrando na tela uma mensagem:
- O PRIMEIRO NÚMERO é maior!
- O SEGUNDO NÚMERO é maior!
- NÃO EXISTE valor maior, os dois são iguais.'''

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 > n2:
    print("O PRIMEIRO NÚMERO é maior!")
elif n2 > n1:
    print("O SEGUNDO NÚMERO é maior!")
else: 
    print("NÃO EXISTE valor maior, os dois são iguais.")