# Aula 08 Desafio 015
# Crie um progrma que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math 

nu = float(input("Digite um número: "))
interio = math.floor(nu)

print("O número é {} e sua parte inteira é {}".format(nu, interio))
