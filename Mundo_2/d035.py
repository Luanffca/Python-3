# Desafio 035 
''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em  QUANTOS ANOS ele vai pagar.

OBS: Calcule o valor da prestação mensal, sabendo que ela não exceder 30% do salário ou então o empréstimo será regado.'''

print("-="*25)
casa = float(input(" Qual o valor da casa que você deseja comprar?\n R$ "))
salario = float(input(" Quanto é o seu salário?\n R$ "))
anos = int(input("Você que pretende pagar em quantos anos? "))
print("-="*25)

meses = anos * 12
prestação = casa / meses
mimino = (salario / 100) * 30

if prestação > mimino:
    print("Seu empréstimo foi negado!")
    print("Seu emprestimo não foi aprovado, pois o valor das parcelas é maior que 30%. E a prestação será de, R${}".format(prestação))
else: 
    print("Empréstimo aprovado.")
    print("O valor da casa é de {}, seu salário: R${}, pagar em {} anos.".format(casa, salario, anos))
    print("O valor da prestação mensal e de R${}.".format(prestação))