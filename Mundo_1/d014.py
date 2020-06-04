# Desafio 014
# Escreva um progrma que pergunte a quantidade de KM percorridos por um carro aludado e a quantidade de dias pelos quais ele foi aludado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos KM rodados? "))

dias_preco = dias * 60
km_rodados = km * 0.15
soma = dias_preco + km_rodados 

print("Você alugou por {} dias e rodou {} km. \n O Valor a ser pago é de R${}.".format(dias, km, soma))
