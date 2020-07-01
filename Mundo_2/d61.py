'''Melhore o DESAFIO 060, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1)*razão
n = primeiro
fim = 0
while (n < decimo + razão):
    print("{} ".format(n), end="-> ")
    n = n + razão
print("ACABOU")
