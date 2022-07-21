import numpy as np
import math

#f = lambda x: x-2**(-x)

# Função de interação
g = lambda x:math.cos(x)-math.e**(-x**2)+x

inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = 1,1.5,10**(-4)
k = inter(a,b,erro)

cont=0
while True:
    x = g(b)
    print('Interação ',cont, math.cos(x), '-', math.e**(-x**2), '+', x, '=', x)
    if np.abs((x-b)/b)<erro:
        break
    b = x
    cont+=1

print("Solução numérica: %f" %x)
print("Interações: %d" %cont)