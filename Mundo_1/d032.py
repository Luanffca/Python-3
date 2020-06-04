# Desafio 032
# Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Segundo valor: "))
# Verificando quem é o nemor. 
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Vereficando quem é o menor. 

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print("O menor número digitado é: {}".format(menor))
print("O maior número digitado é: {}".format(maior))
