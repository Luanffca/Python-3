''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores se for "M" ou "F". Caso esteja errado peça a digitação novamente até ter um valor correto.'''

sexo = str(input("Digite M ou F, refente ao seu sexo: ")).upper().strip()

while sexo not in "MF":
    sexo = str(input("Informação inválida. Por favor, informe seu sexo: ")).upper().strip()
print("Sexo {} registrado com sucesso.".format(sexo))
    
