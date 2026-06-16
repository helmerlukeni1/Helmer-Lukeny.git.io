# Exemplo usando break
for numero in range(1, 10):
    if numero == 5:
        print("Número 5 encontrado. Saindo do loop!")
        break # Para a execução aqui
    print(numero)

# Exemplo usando continue
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue # Pula o número 3 e vai para a próxima repetição
    print(contador)
