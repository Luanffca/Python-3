# Desafio 021 Aula 09
'''Crie um programa que leia o nome completo de uma pesseoa e mostre:
- O nome com todas as letras minúsculas.
- O nome com todas as letras maiúsculas.
- Quantas letras ao todos sem (considerar os espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input("Qual o se nome completo? "))

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
#print(nome.find(' '))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
