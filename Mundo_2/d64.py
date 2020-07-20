'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostrando a média entre todos os valores e qual foi maior e o menor valores lidos. O programa deve pergunta ao usuário se ele quer ou não continuar a digitar valores.'''

r = "S"
soma = quantos = media =0
while r in "S":
    n = int(input("Digite um valor: "))
    soma += n
    quantos += 1
    if quantos ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor: 
            menor = n
    r = str(input("Quer continuar S/N? ")).upper().strip()[0]
media = soma / quantos
print("A média dos números digitado foram: {} ".format(media))
print("A quantidade de números digitados foram: {} ".format(quantos))
print("O maior foi {} e o menor foi {}".format(maior, menor))
print("Fim")
