# Aula Prática 
# Desafios do 35 ao 44
nome = str(input("Qual oseu nome? ")).strip()

if  nome == "Luan":
    print("Que nome Lindo!")
elif nome == "Pedro" or nome == "Maria" or nome == "José":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Cláudia Jéssica Juliana": 
    print("Belo nome feminino.")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}!".format(nome))