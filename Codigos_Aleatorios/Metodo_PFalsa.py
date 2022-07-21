import numpy as np 
import math

# Função
f = lambda x: math.e**(-x**2)-math.cos(x)

# Número de Interações
inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

# Pontos iniciais e erro
a,b,erro = 1,2,10**(-4)

k = inter(a,b,erro)

for i in range(k):
    x = (a*f(b)-b*f(a))/(f(b)-f(a))
    print("Interação" ,i, " x", i,"= ", a ," * ", f(b), " - ", b, " * ", f(a) ," / ", f(b), "-", f(a), "= x =", x, "\n")
    print("Função: ", f(x), "\n")
    if np.abs(f(x)) >= erro:
        if f(a)*f(x)<0:
            b = x
        else:
            a = x
    else:
        break

print("Solução numérica: %f" %x)
print("Interações: %d" %i)