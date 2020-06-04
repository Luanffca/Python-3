# Desafio 025
'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes a apareceu a letra "A".
- Em que posição ela apararece pela primera vez.
- Em que posição ela aparece a última vez.'''

frase = str(input("Digite uma frase: ")).upper().strip()

print("Aparece {} vezes a letra a na frase.".format(frase.count('A')))
print("Sua primeira aparição é na posição {} ".format(frase.find("A")+1))
print("Sua última aparição é na posição {}".format(frase.rfind("A")+1))