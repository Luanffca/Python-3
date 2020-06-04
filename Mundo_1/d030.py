# Desafio 030
''' Desenvolva um programa que leia a distância de uma viagem em Km.
Calcule  o preço da passagem, cobrando R$0,50 por km para viagem de até 200km e R$0,45 para viagens mais longas.'''

km = float(input("Qual é a distância do sua viagem em km: "))

if km <= 200:
    p = km * 0.50
    print("O valor da passsagem é de R${}".format(p))
else:
    p1 = km *0.45
    print("O valor da passagem é de R${}".format(p1))