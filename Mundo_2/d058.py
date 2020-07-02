'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar 
[2] multiplicar
[3] maior
[4] novos números 
[5] sai do programa
Seu programa deverá realizar a operção solicitado em cada caso.'''

pvalor = int(input("Primeiro valor: "))
svalor = int(input("Segundo valor: "))
n = 1
while n == n:
    n = int(input('''    [1] somar 
    [2] multiplicar
    [3] maior
    [4] novos números 
    [5] sai do programa.
    Informe a opição que você escolheu: '''))
    if n == 1:
        soma = pvalor + svalor
        print("Opção {}, fazer a soma de dois valores.".format(n))
        print("A soma de {} e {} igual a {}".format(pvalor, svalor, soma))
        print("-="*20)
    elif n == 2:
        multiplicar = pvalor * svalor
        print("Opção {}, multiplicar dois valores.".format(n))
        print("Multiplicação de {} e {} igual a {}".format(pvalor, svalor, multiplicar))
        print("-="*20)
    elif n == 3:
        print("Opção {}, diz quem é o maior valor.".format(n))
        if pvalor > svalor:
            print("O maior valor é {}".format(pvalor))
        elif svalor > pvalor:
            print("O maior valor é {}".format(svalor))
        else:
            print("Os dois números são iguais.")
        print("-="*20)
    elif n == 4:
        print("Opção {}, escolher dois novos valores.".format(n))
    elif n == 5: 
        print("Você escolheu a opção sair do programa.")
        print("-="*20)
        break
    else: 
        print("Opção inválida. Tente novemente.")
        print("-="*20)
print("Fim")
