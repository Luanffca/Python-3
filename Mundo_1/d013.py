# Desafio 013 
# Escreva um progrma que converta uma temperatura digitada em Cº e converta para ºF.

c = float(input("Informe a temporatura em Cº: "))

f = ((9*c)/5)+32
print("A temperatura de {}ºC corresponde a {}ºF!".format(c, f))
