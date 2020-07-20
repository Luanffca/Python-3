'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os primeiros elementos de uma SEGUÊNCIA DE FIBONACCI. 
EX: 0 _ 1 _ 1 _ 2 _ 3 _ 5 _ 8'''

n = int(input("Quantos elementos desejar ver? "))
c = 0 
d = 1
a = 0
if n % 2 == 0: 
    while a != n:
        print(c, d, end=" ")
        c += d
        d += c
        a += 2
if n % 2 != 0:
    while a != (n+1):
        print(c, "" if a == (n -1 ) else d, end=" ")
        c += d
        d += c
        a += 2 

'''ou
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0 
t2 = 1
print = "{} ~ {}" .format((t1, t2), end=" ")
cont = 3
while <= n:
    t3 = t1 = t2
    print(" ~ {}!".format(t3), end=" ")
    t1 = t2
    t2 = t3
    cont += 1
print(Acabou)'''