# Desafio 003
# Faça um progrma que leia pelo teclado e mostre na tela o seu tipo primitivo e todas as informações  possiveis sobre ela.

algo = input("Digite algo: ")

print("O tipo primitio desse valor é ", type(algo))
print("É alfabético? ", algo.isalnum())
print("É número? ", algo.isnumeric())
print("Está em maiúsculo? ", algo.isalpha())
print("Está em minúsculo? ", algo.islower())
print("É capitalizada? ", algo.istitle())
print("Só tem espaços? ", algo.isspace())
