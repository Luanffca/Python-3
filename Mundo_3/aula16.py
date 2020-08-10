# Exercícios 

# Exemplo 1: Printa tudo o que está na Tupla.
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(lanche)'''

# Exemplo 2: Printa somente aquele que está na posição escolhida.
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(lanche[1])'''

# Exemplo 3: Printa somente aquele que está na posição escolhida só que de outra forma.
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(lanche[-3])'''

# Exemplo 4: O print vai do elemento um ao elemento 3, desconsiderando o último.  
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(lanche[1 : 3])'''

# Exemplo 5: O print vai do elemento 2 ao final.  
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(lanche[2:])'''

# Exemplo 5: O print vai do elemento do começo ao elemento 2, desconsiderando o último valor.  
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(lanche[:2])'''

# TUPLAS SÃO IMUTÁVEIS

# TIPOS DE FOR EM  TUPLAS:

# EXEMPLO 1: SEM MOSTRA A POSIÇÃO 
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
for comida in lanche:
    print(f'Eu vou comer {comida}')'''

# EXEMPLO 2: MOSTRANDO A POSiÇÃO
''''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

# EXEMPLO 3: MOSTRANDO A POSiÇÃO
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

# EXEMPLO 4: MOSTRANDO A POSiÇÃO INICIANDO DO 1
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont + 1}')'''

# OUTROS EXEMPLOS

# EXEMPLO 1: EM ORDEM ALFABETICA
'''lanche = ("Hambúrquer", "Suco", "Pizza", "Pudim")
print(sorted(lanche))'''

# EXEMPLO 2:
'''a = (2, 5 ,4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c)) # LER O TAMANHO DA TUPLA.
print(c.count(5)) # LER QUANTAS VEZES APARECE O NÚMERO NA TUPLA.
print(c.index(8)) # LER A POSIÇÃO ONDE ELE ESTAR.'''

# EXEMPLO 3:
'''pessoas = ('Luan', 18, "M", 75.75)
del(pessoas)
print(pessoas)'''