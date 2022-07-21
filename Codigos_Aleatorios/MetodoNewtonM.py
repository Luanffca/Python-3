# Luan Fernandes de França
def funcao(x):
    return (x**3)-(3*x)+3 
    # return (x**5)-(3.7*(x**4))+(7.4*(x**3))-(10.8*(x**2))+(10.8*x)-6.8

def newton_Poli(a, x, epsilon, itermax):
    n = len(a)-1
    # print("K\t\tx\t\tpn(x)")
    for k in range(itermax):
        b = a[n]
        c = b
        for j in range(n-1, 0, -1):
            b = a[j] + b*x
            c = b + c * x
        b = a[0] + b*x
        # print("%d\t%e\t%e" %(k,x,b))
        if abs(b) <= epsilon:
            print('\n\n|F(x)|:', abs(b))
            return(False, x)
        print('|F(x)|:',abs(b), "\n")
        print(round(x, 9), '- (', round(b, 9), '/', round(c, 9),')')
        x = round(x - (round(b,9)/round(c,9)), 9)
    
    print("Número máximo de intereções atingido")
    return (True, x)
# a =  [-6.8, 10.8, -10.8, 7.4, -3.7, 1]
a = [3,-3,0,1]
x0 = -0.8
epsilon = 0.000001
itemax = 30

(houveErro, raiz) = newton_Poli(a, x0, epsilon, itemax)
if houveErro:
    print("O Método de Newton_Polinômios retornou um erro.")
if raiz:
    print("Raiz encontrada: %s" %raiz)

