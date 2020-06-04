# Desafio 034
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

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
else:
    print("Os segmentos acima não podem formar um triângulo!")