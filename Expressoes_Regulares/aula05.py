# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
from operator import attrgetter
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1\3\4', texto))
# print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', texto))
# print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto))

# tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto)
# pprint(tags)
# for tag in tags:
#     um,dois, tres= tag
#     print(tres)


# tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# pprint(tags)

# cpf = 'a 123.456.789-12ca '
# print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}',cpf))

# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})',cpf))