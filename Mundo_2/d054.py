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
    