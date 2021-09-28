# Desafio 037 
'''Escreva um programa que leia um número inteiro qualquer e peçã para o usuário escolher qual será a base de conversão. 
A - binário
B - octal 
C - para Hexadecimal '''

nu = int(input("Digite um número inteiro: "))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opção = int(input("Qual a sua opção: "))

if opção == 1:
    print("{} concertido para BINÁRIO é igual a {}".format(nu, bin(nu)))
elif opção == 2:
    print("{} convertido para OCTAL é igual a {}".format(nu, oct(nu)))
elif opção == 3:
    print("{} convertido para HEXADECINAL é igual a {}".format(nu, hex(nu)))
else:
    print("Opção Invalida. Tente novamente.")