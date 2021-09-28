# import json
# data = [1,2,3,4,5]
# with open('no.json', 'w') as txtfile:
#     json.dump(data, txtfile)
    # json.dump(c, file)
    # json.dump(os.path.getsize(c), file)
    # json.dump('\n', file)


import json


lista_salva = [
    dict(arquivo=obj.aquivo, tamanha=obj.aquivo)
    for obj in list_arquivos
]

dict_salve = {"Litas": lista_salva}
dict_salve = json.dumps(dict_salve, indent=4, sort_keys=False)

try:
    lista = open("lista.json", 'w')
    lista.write(dict_salve)
    lista.close()
except Exception as erro:
    print("Ocorreu um erro ao carregar o arquivo")
    print("O erro é: {}". format(erro))