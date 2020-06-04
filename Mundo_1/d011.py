# Desafio 011 
# Faça um algoritmo que leia o preço de um produto  e mostre seu novo preço com 5% de desconto.

preço = float(input("Qual é o preço? R$ "))

desconto = preço - (preço * 5 / 100)
print("O desconto é de = R${:.2f}.".format(desconto))
