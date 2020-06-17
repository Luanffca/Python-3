''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 1000
for c in range(1,6):
    p = float(input("Digite o peso da pessoa {}: Kg ".format(c)))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print(" O maior peso é Kg {}.\n O menor peso é Kg {}".format(maior, menor))

''' ou 
maior = 0
menor = 0
for c in range(1,6):
    p = float(input("Digite o peso da pessoa {}: Kg ".format(c)))
    if c == 1 :
        maior = c
        menor = c
    else:
        if p > maior:
            meior = p
        if p < menor:
            menor = p
print("O maior peso lido foi de {}kg".format(maior))
print("O menor peso lido foi de {}kg".format(menor))'''