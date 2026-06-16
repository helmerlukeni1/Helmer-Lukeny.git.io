# Solicita o valor em metros ao usuário e converte para número decimal (float)
metros = float(input("Digite o valor em metros: "))

# Realiza as conversões
centimetros = metros * 100
milimetros = metros * 1000

# Apresenta os resultados na tela
print(f"{metros} metro(s) equivale(m) a:")
print(f"- {centimetros:.0f} centímetros")
print(f"- {milimetros:.0f} milímetros")
