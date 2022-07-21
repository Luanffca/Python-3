import numpy as np 
import mpmath as mp
import math
mp.dps = 15; mp.pretty = True

# f = lambda x: math.e**(-x**2)-math.cos(x)
# g = lambda y: -2 * math.e**(-y**2)- math.sin(y)
f = lambda x: x**3 - 3*x + 3
inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

a,b,erro = -3,-1.5,10**(-6)
k = inter(a,b,erro)

for i in range(k):
    x = a-(f(a)/mp.diff(f,a))
    fa =float(f(a))
    print("Interação" ,i, " x", i,"= ", a ,"(", fa ,"/", mp.diff(f,a), ") = ", x ,"\n")
    fv = f(x)
    print("Função de X", i ," = ", fv,"\n")
    if np.abs((x-a)/a)<erro:
        break
    a = x

print("Solução numérica: %f" %x)
print("Interações: %d" %i)