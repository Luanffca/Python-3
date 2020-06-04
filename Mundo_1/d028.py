# Desafio 028
'''Escreva um programa que leia velocidade de um carro.
Se ele ultrapassar 80KM/h, mostre uma mensagem que o carro foi multado.
A multa vai custar R$7,00 por cada KM acima do limite.'''

km = float(input("Informe em quantos km/h você estava. "))

multa = (km - 80) * 7 

if  km > 80:
    print("Você foi multado.")
    print("O valor da multa e de R${}".format(multa))
else:
    print("Você não foi multado.\nDigira com cuidado.")
