''' Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são miores.
Maior idade 21 anos'''

from datetime import date
year = 0
menor = 0

for c in range(1,8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    y = date.today().year - ano
    if y >= 21:
        year += +1
    else:
        menor += 1
print(" São maior de idade {} e {} não são.".format(year, menor))

