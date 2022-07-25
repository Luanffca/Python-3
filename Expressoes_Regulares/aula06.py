# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação


import re

cpf = '123.456.789-12'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})',cpf))
print(re.findall(r'[^a-z0-9A-Z.-]+',cpf))