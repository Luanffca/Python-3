# Aula Prática 
# Desafios do 65 ao 71
# Revisão
'''cont = 1
while cont <= 10:
    print(cont, " -> ", end=" ")
    cont += 1
print('Acabou')'''

# Exemplo 1
n = s = 0
while True:
    n = int(input("Digite um número: ")) 
    if n == 999:
        break 
    s += n
print(f"A soma vale {s}")

