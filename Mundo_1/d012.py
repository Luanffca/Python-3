# Desafio 012 
# Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o seu salário? R$ "))

almento = salario + (salario * 15 / 100)
print("O desconto é de = R${:.2f}.".format(almento))
