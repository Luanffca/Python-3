#   Exercício Python 073 - Tuplas com Times de Futebol
#   Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#   na ordem de colocação. Depois mostre:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = 'Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthians', 'Flamengo', 'Atlético Mineiro', 'Athletico Paranaense', 'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo', 'Fluminense', 'Vasco da Gama', 'Bhaia', 'Sport', 'Vitória', 'Ponte Preta', 'América', 'Coritiba' 

while True:
    print("-+"*40)
    print("Tabela do Campeonato Brasileiro de Futebol 2019")
    print("-+"*40)
    print('''A) Os 5 primeiros times.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
E) Fecha o programa. ''')
    print("-+"*40)
    opção = " "
    while opção not in "ABCDE":
        opção = str(input("Qual sua opção: ")).upper().strip()[0]
    if opção == "A":
        for time in range(0, 5):
            print(f'{time + 1}º posição {times[time]}')
    elif opção == "B":
       for time in range(16, 20):
            print(f'{time + 1}º posição {times[time]}')
    elif opção == "C":
        print(sorted(times))
    elif opção == "D":
        print(f'Chapecoense está na posição {times.index("Chapecoense")+1}')
    elif opção == "E":
        break
print("Você encerrou sua pesquisa sobre o Campeonado Brasileiro de Futebol de 2019")

