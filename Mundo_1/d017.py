# Desafio 017 
# Faça um progrma que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians 

angulo = float(input("Informe o ângulo: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(" O ângulo é {:.2f}.\n Seu seno é {:.2f}. \n Seu cosseno {:.2f}.\n E seu tangente {:.2f}".format(angulo, seno, cosseno, tangente))
