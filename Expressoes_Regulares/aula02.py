# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'joão|João|Maria|ad....s', texto))
print(re.findall(r'[jJ]oão|[Mm]aria|ad....s', texto))
print(re.findall(r'[A-Z]oão', texto))
print(re.findall(r'[a-zA-Z]oão', texto))
print(re.findall(r'joão|MaRia', texto, flags=re.IGNORECASE))

