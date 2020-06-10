''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo. 
Qual é o nome do homem mais velho. 
Quantas mulheres tem menos de 20 anos.  '''

s = 0
i = 0
m = 0
cont = 0

for c in range(1,5):
    nome = str(input("NOME: ")).strip().upper()
    idade = int(input("IDADE: "))
    sexo = str(input("Digite M para o sexo masculino e F para feminino: ")).strip().upper()
    print("-="*30)
    s += idade
    media =  s / 4
    if sexo == "F" and idade < 20:
        cont += +1 
    if sexo == "M":
        if idade > m:
            m = idade 
            n = nome
    else:
        nom = "Não existe Homem na lista."
print("Homem mais velho: {}".format(n))
print("Média de idade do grupo: {}".format(media))
print("Quatidade de mulheres menor de 20 anos: {}".format(cont))