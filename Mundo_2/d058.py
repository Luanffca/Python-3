'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar 
[2] multiplicar
[3] maior
[4] novos números 
[5] sai do programa
Seu programa deverá realizar a operção solicitado em cada caso.'''

n = 1
while n == n:
    pvalor = int(input("Primeiro valor: "))
    svalor = int(input("Segundo valor: "))
    n = int(input('''
    [1] somar 
    [2] multiplicar
    [3] maior
    [4] novos números 
    [5] sai do programa.
    Informe a opição que você escolheu: '''))
    if n == 1:
        soma = pvalor + svalor
        print("Opção {}, fazer soma de dois valores.".format(n))
        print("Soma de {} e {} igual a {}".format(pvalor, svalor, soma))
        break
    elif n == 2:
        multiplicar = pvalor * svalor
        print("Opção {}, multiplicar dois valores.".format(n))
        print("Multiplicação de {} e {} igual a {}".format(pvalor, svalor, multiplicar))
        break
    elif n == 3:
        if pvalor > svalor:
            print("O maior valor é {}".format(pvalor))
        elif svalor > pvalor:
            print("O maior valor é {}".format(svalor))
        else:
            print("Os dois números são iguais.")
        break
    elif n == 4:
        print("Opção {}, escolher dois novos valores.".format(n))
    else: 
        print("Você escolheu a opção sair do programa.")
        break 
print("Fim")
