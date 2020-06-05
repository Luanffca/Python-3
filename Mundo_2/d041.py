# Desafio 041
'''Refaça o DESAFIO 034 dos Triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados são iguais.
- Isósceles: Dois lados iguais.
- Escaleno: todos os lados diferentes.'''

print("-="*20)
print("Analizador de Triângulos!")
print("-="*20)
d1 = float(input("Primeiro segmento: "))
d2 = float(input("Segundo segmento: "))
d3 = float(input("Teceiro segmento: "))
print("-="*20)
print("Analizando se forma Triângulos!")
print("-="*20)

if d1 < d2 + d3 and d2 < d1 + d3 and d3 < d1 + d2:
    print("Os segmetos acima podem formar um triângulo!")
    print("-="*20)
    if d1 == d2 == d3:
        print("Todos lados são iguais portando esse triângulo é Equilátero.")
    elif (d1==d2) or (d1==d3) or (d2==d3):
        print("Dois falos iguais potanto esse triângulo é Isósceles.")
    elif d1 != d2 != d3 != d1:
        print("Todos os lados são diferentes por tanto esse triângulo é Escaleno.")

else:
    print("Os segmentos acima não podem formar um triângulo!")