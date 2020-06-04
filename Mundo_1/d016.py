# Desafio 016 
# Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

from math import hypot

catetoop = float(input("Informe o cateto aposto: "))
catetoad = float(input("Informe o cateto adjacente: "))

print("A hipotenuza do triângulo tem o tamanho de {:.2f}".format(hypot(catetoop, catetoad)))
