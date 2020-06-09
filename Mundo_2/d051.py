''' Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo. '''

num = int(input("Digite um número: "))
x = 0
for c in range(1, num):
    if num % c == 0:
        x = x + 1
        if x > 1:
          break
if x > 1:
  print("Não é primo.")
else:
  print("É primo.")
