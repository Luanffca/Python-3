# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles. (DESCONSIDERANDO O FLAG) 

print("Condição de parada 999.")
print("~"*30)
s = t = 0
while True:
    n = int(input("Valor: "))
    if n == 999:
        break
    t += 1
    s += n
print(f" A soma de todos os valores digitados foi {s}.\n Você digitou {t} valores.")
