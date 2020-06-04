#  Desafio 010
# Faça um programa que leia a largura e a alura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# OBS: sabendo que cada litro de tinta pinta uma área de 2m**2

lagura_da_parede = float(input("Qual a largura da sua padere? "))
altura_da_parede = float(input("Qual a altura da sua parede? "))

area = lagura_da_parede * altura_da_parede
tinta = area / 2

print("Sua parede tem a dimenssão de {} x {} e sua área é de {}m2.".format(lagura_da_parede, altura_da_parede, area))
print("Para pintar essa parede, você precisa de {:.2f} de tinta.".format(tinta))