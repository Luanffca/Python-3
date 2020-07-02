'''Faça um programa que leia um  número qualquer e mostre o seu fatorial. 
ex: 
5! = 5x4x3x2x1=120'''

n = int(input("Digite um número: "))
c = 1
f = 1
while c <= n:
    f *= c
    c += 1
print("FATORIAL = {}".format(f))
