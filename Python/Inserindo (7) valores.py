# Cria a lista principal contendo duas sublistas: [pares, ímpares]
num_lista = [[], []]
valor = 0

# Solicita os 7 valores ao usuário
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    
    # Verifica se é par ou ímpar e adiciona na sublista correspondente
    if valor % 2 == 0:
        num_lista[0].append(valor)
    else:
        num_lista[1].append(valor)

# Ordena as listas de forma crescente
num_lista[0].sort()
num_lista[1].sort()

# Exibe os resultados
print("-" * 30)
print(f"Valores pares em ordem crescente: {num_lista[0]}")
print(f"Valores ímpares em ordem crescente: {num_lista[1]}")
