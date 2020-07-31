'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada serão entregues. 
OBS. Considerando que o caixa posssui cédulas de R$50, R$20, R$10, e R$1 '''

print("+"*50)
print("{:^50}".format("BANCO PYTHON"))
print("+"*50)
valor = int(input("Informe o valor que você deseja sacar: R$ "))
total = valor
cedula = 50
cedulatotal = 0
while True:
    if total >= cedula:
        total -= cedula
        cedulatotal += 1
    else:
        if cedulatotal > 0:
            print(f"Todal de {cedulatotal} cédulas de R$ {cedula}") 
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cedulatotal = 0
        if total == 0:
            break
print("VOLTE SEMPRE.")