# Desafio 031
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input("Ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Sim esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")
