# QUESTAO 02

num = int(input("Digite um número: "))

fib_ant_ant = 0  # valor inicial da sequência de Fibonacci
fib_ant = 1
fib_atual = fib_ant_ant + fib_ant

while fib_atual < num:
    fib_ant_ant = fib_ant
    fib_ant = fib_atual
    fib_atual = fib_ant_ant + fib_ant

if fib_atual == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")


# QUESTAO 04
faturamento = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

total_faturamento = sum(faturamento.values())

percentual = {}

for estado, valor in faturamento.items():
    percentual[estado] = (valor / total_faturamento) * 100

print(percentual)

# QUESTAO 05
string = input("Digite uma string para inverter: ")  # ou defina a string diretamente

string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("A string invertida é:", string_invertida)
