
# valor = int(input("Informe o Numero para ser sua Tabuada: "))

# print("----- TABUADA -----")
# for i in range(10):
#     print("     %d x %d = %d" %(valor, i+1, valor*(i+1)))

media = float(input("Informe a Media: "))

if media >= 7:
    print("Voce foi APROVADO com %.2f" % media)
elif media < 7 and media >= 3:
    print("Voce esta de Recuperacao com %.2f" % media)
else:
    print("Voce foi Reprovado com %.2f" % media)
