# # Método de Horner
# # Data equação polinomial x**5 - 3.7x**4 + 7.4x**3 - 10.8x**2 + 10.8x - 6.8 = 0 questão
#                         # [-6.8, 10.8, -10.8, 7.4, -3.7, 1]
# # Codificar x**3-3*x+3
# #           [3,-3,1]
# a = [-6.8, 10.8, -10.8, 7.4, -3.7, 1] 
# n  = len(a)-1 # O Grau do polinômio
# z = 1.5

# # inicializar a variavel
# b = a[n]
# c = b
# for j in range(n-1, 0, -1):
#     b = a[j] + b*z
#     c = b + c * z
# b = a[0] + b*z
# print("O valor do polinômios é: %s e o valor da derivada é: %s" %(b, c))



# def newton_Poli(a, x, epsilon, itermax):
#     n = len(a)-1
#     print("K\t\tx\t\tpn(x)")
#     for k in range(itermax):
#         b = c = a[n]
#         #c = b
#         for j in range(n-1, 0, -1):
#             b = a[j+1] + b*x
#             if(j < 2):
#                 c = b + c * x
#             #c = b + c * x
#         #b = a[0] + b*x
#         print("%d\t%e\t%e" %(k,x,b))
#     if abs(b) <= epsilon:
#         return(False, x)
#     x = x - (b/c)
#     print("Número máximo de intereções atingido")
#     return (True, x)

# a = [-6.8, 10.8, -10.8, 7.4, -3.7, 1]
# # a = [3,-3,1]
# x0 = -0.8
# epsilon = 0.000001
# itemax = 30

# (houveErro, raiz) = newton_Poli(a, x0, epsilon, itemax)

# if houveErro:
#     print("O Método de Newton_Polinômios retornou um erro.")
# if raiz:
#     print("Raiz encontrada: %s" %raiz)

#print((0.337606838**3)- (9*0.337606838) + 3)


#print(round(x, 9), '- (', round(b, 9), '/', round(c, 9),')')
        # print('|F(x)|:', abs(b), "\n\n")
        # x = round(x - (round(b,9)/round(c,9)), 9)

def funcao(x):
       return (x**3)-3*x+3
 
def metodo(x,a,precisao,itmax):
   for k in range(itmax):
       print('\033[1;29;39m{}\n\t    |{}|\033[0;;m'.format('-=-'*10,k))
       b = c = a[0]
       f = funcao(x)       
       print("  _\n  X:    {}".format(round(x,9)))
       for i in range(0,len(a)-1):
           b = a[i+1] + b * x
           if(i < len(a)-2):
               c = b + c * x
       if abs(b) < precisao:
           print(' \033[1;33;48m|F(x)|:',abs(f))
           print('\033[1;29;39m-=-'*10,'\n\t    FIM')
           break
       x = round(x - (b/c), 9)
       if abs(x) < precisao:
           print('\033[1;33;48m',abs(x))
           break
       k = k + 1
      
metodo(-0.8,[1,0,-3,3],0.00001,30)
#metodo(-2,[1,0,-3,3],0.00001,10)