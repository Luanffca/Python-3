''' Refaça o DESAFIO 008, mostrando de um número que usuário escolha, só que agora utilizando um laço for.'''

num = int(input("Digite o número: "))
print("=="*25)


for c in range(1, 11):
    print("A tabuada de {} e de {} é igual a: {} ".format(num, c, num * c ))
print("=="*25)
