# Desafio 018 
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nomes deles e escrevendo o nome do esconhido.

from random import choice

nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome: "))
nome4 = str(input("Digite o quarto nome: "))
 
print("O nome do aluno sorteado foi {}".format(choice([nome1, nome2, nome3, nome4])))
