#040
''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
- Até 9 anos: MIRIN
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIO 
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date

print("-="*40)
ano = int(input("Para mostrar sua categoria precisamos saber o ano em que vcoê nasceu!\nAno: "))
print("-="*40)
print("")

y = date.today().year - ano

if y <= 9:
    print("Sua categoria é a MIRIM.")
elif y >= 10 and y <= 14: 
    print("Sua categoria é a INFANTIL.")
elif y >= 15 and y <= 19:
    print("Sua categoria é a JUNIO.")
elif y == 20:
    print("Sua categoria é a SÊNIOR.")
elif y > 20:
    print("Sua categoria é a MASTER.")