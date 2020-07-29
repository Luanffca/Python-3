''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A - Qual é o total gasto na compra. 
B - Quantos produtos custava mais de R$ 1000. 
C- Qual e o nome do produto mais barato. '''
total = maior = barato = cont = 0
nomepro = ''
while True:
    print("-+"*20)
    nome = str(input("Nome do Produto: "))
    preço = float(input("Valor do Produto: R$ "))
    cont += 1
    total += preço
    if preço > 1000:
        maior += 1
    if cont == 1:
        barato = preço
        nomepro = nome
    else:
        if preço < barato:
            barato = preço
            nomepro = nome
    opção = " "
    while opção not in 'SN':
        opção = str(input("Deseja continuar S/N: ")).upper().strip()[0]
    if opção == "N":
        break
print("-+"*20)
print(f"O valor total gasto é de R$ {total}.")
print(f"Tem {maior} produtos que custa mais de R$1000.")
print(f"O produto mais barato foi {nomepro} e custa R$ {barato}")
