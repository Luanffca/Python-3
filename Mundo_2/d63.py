'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (DESCONSIDERANDO O FLAG).'''

print("Condição de parada é 999.")
n = 1
soma = 0 
total = 0
while n != 999:
    n = int(input("Digite um valor: "))
    if n != 999:
        soma += 1
        total = total + n
print("Você digitou {} termos e a soma  de todos eles é {}".format(soma, total))
