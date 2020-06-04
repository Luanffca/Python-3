# Desafio 009 
# Crie um programa que leia quanto dinherio uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. 
#    Obs: Contação do dolar : 3,27

dinheiro = float(input("Quanto você tem na carteira? R$ = "))

print("Seu dinheiro em R$ {} e em US$ é = {:.2f}".format(dinheiro, dinheiro / 3.27))
