def funcao(x):
    return (x**3)-(3*x)+3
    # return (x**5)-(3.7*(x**4))+(7.4*(x**3))-(10.8*(x**2))+(10.8*x)-6.8

def metodo(x,a,precisao,itmax):
    for k in range(itmax):
        print('\033[1;29;39m{}\n\t    |{}|\033[0;;m'.format('-=-'*10,k))
        b = c = a[0]
        f = funcao(x)
        print("  _\n  X:    {}".format(round(x,9)))
        
        for i in range(0,len(a)-1):
            b = a[i+1] + b * x
            if(i < 2):
                c = b + c * x
        if abs(b) < precisao:
            print(' \033[1;33;48m|F(x)|:',abs(b))
            print('\033[1;29;39m-=-'*10,'\n\t    FIM')
            break
        #print(' \033[1;33;48m|F(x)|:',abs(b))
        deltax = b/c
        x = round(x - deltax, 9)
        if abs(x) < precisao:
            print('\033[1;33;48m',abs(x))
            break
        k = k + 1
        print(round(f,9))

# metodo(1.5,[1,-3.7,7.4,-10.8,+10.8,-6.8],0.00001,5)
metodo(-0.8,[1,0,-3,3],0.00001,30)
# metodo(-2,[1,0,-3,3],0.00001,10)