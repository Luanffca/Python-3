import numpy as np 
import math

f = lambda x: math.e**(-x**2)-math.cos(x)

# Número de interações
inter = lambda a,b,erro: 1 + int((np.log(b-a)-np.log(erro))//np.log(2))

# Pontos iniciais e erros
a,b,erro = 1,2,10**(-4)

k = inter(a,b,erro)

if f(a)*f(b)>0:
    print("A função tem o mesmo sinal nos pontos a e b")
else:
    for i in range(k):
        x = (a+b)/2
        ne = (b-a)/2
        print ("x",i,"=", a, "+", b, "/", 2, " = x",i, "= ", x )
        fv = f(x)
        print("Função de X", i ," = ", fv,"\n")
        if f(x)==0 or ne<erro:
            break
        else:
            if f(a)*f(x)<0:
                b = x
            else:
                a = x

print("Solução numérica: %f" %x)
print("Interações: %d" %i)