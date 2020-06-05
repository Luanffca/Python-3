# Desafio 042 
'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal 
- 25 até 30: Sobrepeso 
- 30 até 40: Obesidade 
- Acima de 40: Obesidade Mórbida'''

print("-="*30)
print("Para Calcular seu IMC presisamos saber sua ALTURA E PESO.")
print("-="*30)
peso = float(input("PESO: "))
altura = float(input("ALTURA: "))
print("-="*30)
print(" ")
imc = peso / (altura * altura)
print(" Tabela de IMC!\n - Abaixo de 18.5: Abaixo do peso.\n - Entre 18.5 e 25: Peso ideal.\n - 25 até 30: Sobrepeso.\n - 30 até 40: Obesidade.\n - Acima de 40: Obesidade Mórbida.")
print("-="*30)
print(" ")
if imc < 18.5:
    print("Abaixo do peso!\nIMC = {:.1f}".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Peso ideal!\nIMC = {:.1f}".format(imc))
elif imc >= 25 and imc < 30:
    print("Sobrepeso!\nIMC = {:.1f}".format(imc))
elif imc >= 30 and imc < 40:
    print("Obesidade!\nIMC = {:.1f}".format(imc))
else:
    print("Obesidade Mórbida!\nIMC = {:.1f}".format(imc))