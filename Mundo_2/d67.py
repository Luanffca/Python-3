# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consequistou no final do jogo.
from random import randint
vitoria = 0
print("-+"*20)
print("JOGO DE ÍMPAR OU PAR.")
print("-+"*20)
while True:
    valor = int(input("VALOR: "))
    computador = randint(1, 10)
    soma = valor + computador
    opção = " "
    while opção not in "PI":
        opção = str(input("ÍMPAR OU PAR (P/I): ")).upper().strip()[0]
        print(f"VOCÊ JOGOU {valor} E O COMPUTADOR {computador}. A SOMA FOI DE {soma}.")
        print("-+"*20)
    if opção == "P":
        if soma % 2 == 0:
            print("VITÓRIA!")
            vitoria += 1
        else:
            print("GAME OVER!")
            break
    if opção == "I":
        if soma % 2 == 1:
            print("VITÓRIA!")
            vitoria += 1 
        else:
            print("GAME OVER")
            break
    print("VAMOS JOGAR NOVAMENTE...")
    print("-+"*20)
print(f"VOCÊ GANHOU {vitoria} VEZES CONSECUTIVA.")
