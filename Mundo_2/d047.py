'''Faça uma programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

s = 0
for c in range(1, 500):
    if c % 2:
        if not (c % 3):
            s += c
print("O somatório de todos os valores foi {}".format(s))
