# Método da Secante imprimindo interação a interação 

import numpy as np 
import math

f = lambda x: math.e**(-x**2)-math.cos(x)

inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = 1,2,10**(-4)
k = inter(a,b,erro)

for i in range(k):
    
    #x = b -f(b)*(a-b)/(f(a)-f(b))
    fb = float(f(b))
    fa =float(f(a))
    x = ((a * f(b))-(b*f(a)))/ (f(b)-f(a))
    print("Interação" ,i, " x", i,"= ", a ," * ", fb, " - ", b, " * ", f(a) ," / ", f(b), "-", f(a), "x =", x, "\n")

    if np.abs((x-b)/b)<erro:
        break
    
    a = b
    b = x 
    
print("Solução numérica: %f" %x)
print("Interações: %d" %i)