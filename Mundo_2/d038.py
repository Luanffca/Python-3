# Desafio 038 
'''Faça uma programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade.
- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE ALISTAR.
- Se já PASSOU DO TEMPO do alistamento.
OBS: Seu programa também deverá mostrar o tempo que falto ou que passou do prazo.'''

print("")
idade = int(input("Qual sua idade? "))
print("=="*15)
print("")
if idade == 18:
    print("Chegou sua hora de se alistar ao serviço militar.")
elif idade < 18:
    falta = 18 - idade 
    print("Você ainda é novo para se alistar.")
    print("Falta {} anos para você se alistar.".format(falta))
else:
    falta = idade - 18  
    print("Você já passou da idade de se alista!")
    print("Já faz {} anos que era para você ter se alistado.".format(falta))