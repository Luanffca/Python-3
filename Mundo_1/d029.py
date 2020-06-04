# Desafio 029
# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.

num = int(input("Informe o número para saber se ele é ínpar ou par: ")) 

resto = num % 2

if resto == 0: 
    print("O número {} é par!".format(num))
else: 
    print("O número {} é ímpar!".format(num))
