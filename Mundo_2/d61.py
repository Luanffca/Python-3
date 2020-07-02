'''Melhore o DESAFIO 060, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro + (10 - 1)*razão
c = 1
print("Condição de parada igual á 0.")
while c <= 10:
    print("{}º Termo = {} ".format(c, primeiro), end="-> ")
    primeiro = primeiro + razão
    c += 1 
m = 1 
while m != 0:
    m = int(input("Deseja mostrar maistermos? Quantos? "))
    d = c
    while d <(c + m):
        print("{}º Termo = {}".format(d, primeiro), end="-> ")
        primeiro = primeiro + razão
        d += 1 
print("FIM DO PROGRAMA")
