# Desafio 039 
'''Crei um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média.
- Média abaixo de 5.0: REPROVADO.
- Média entre 5.0 e 6.9: RECUPERAÇÃO.
- Média 7.0 ou superior:  APROVADO.'''

print("")
nota1 = float(input("Qual sua primeira nota: "))
nota2 = float(input("Qual sua segunda nota: "))
print("=="*20)
print("")

media = (nota1 + nota2 ) / 2 

if media >= 7 and media <= 10:
    print("Você foi APROVADO.\nSua média foi de {:.1f}".format(media))
elif media >= 5.0 and media <= 6.9:
    print("Você está de RECUPERAÇÃO.\nSua média foi de {:.1f}\nEstude para as provas de recupeção.".format(media)) 
else:
    print("Você está REPROVADO.\nSua média foi de {:.1f}\nEstude mais.".format(media))