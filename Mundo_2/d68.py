''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
A - Quantas pessoas tem mais de 18 anos. 
B - Quantos homens foram cadastrados. 
C - Quantas mulheres tem menos de 20 anos. '''
mulher = masculino = maior = 0
while True:
    print("-+"*20)
    idade = int(input("Qual sua idade: "))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input("Sexo: ")).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == "M":
        masculino += 1
    if sexo == "F" and idade < 20:
        mulher += 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continua S/N: ")).upper().strip()[0]
    if resposta == "N":
        break
print("-+"*20)
print(f"Tem {maior} pessoas com mais de 18 anos.")
print(f"Tem {masculino} homens cadastrados.")
print(f"Tem {mulher} mulheres com menos de 20 anos.")
print("-+"*20)
