numero = int(input("Digite um número inteiro positivo: "))

if numero >= 0:
    # O range conta do número digitado até 0
    # O -1 indica que a contagem é decrescente e inclui o 0
    for i in range(numero, -1, -1):
        print(i)
    print("Fim da contagem!")
else:
    print("Por favor, digite um número positivo.")
