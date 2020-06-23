''' Melhore o jogo do DESAFIO 027 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinha até acerta, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

num = randint(0, 10)
n = 1
soma = 0
while n != num:
    n = int(input("Informe um número de 0 a 10. "))
    soma += 1
    if n == num:
        print("Você venceu!!!")
    else:
        print("Você errou.")
        print("Tente novamente até acerta.")

print('Você tentou {} vezes, para ganhar.'.format(soma))
