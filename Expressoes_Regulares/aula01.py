import re

# findall -> vai encontrar todas as ocorrencias da expressao do padrao que quero encontrar dentro do texto
# search -> vai encontrar e primeira ocorrencias e retorna em qual indice que ele encontrou / retorna um objeto met  
# sub -> substituicao 
# compile -> compilar as expressoes e reutilizar as expressoes.


string = 'Este e um teste de expressoes teste regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste','abc', string))

regular = re.compile(r'teste')
print(regular.search(string))
print(regular.findall(string))
print(regular.sub('DEF', string))