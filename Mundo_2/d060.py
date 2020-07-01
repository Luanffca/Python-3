'''Refaça o DESAFIO 050, lendo o primeiro termo e a razão de uma PA, mostrando os 10 progressão usando a estrutura while. '''

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1)*razão
n = primeiro
while (n < decimo + razão):
    print("{} ".format(n), end="-> ")
    n = n + razão
print("ACABOU")
