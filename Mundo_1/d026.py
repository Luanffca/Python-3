# Desafio 026
'''Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida
o primeiro nome e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro : Ana 
último: Souza'''

nome = str(input("Informe seu nome completo: ")).strip()

n = nome.split()

print("Seu primeiro nome é {}".format(n[0]))
print("Seu último nome é {}".format(n[len(n)-1]))
