
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"Você é menor de idade. Faltam {18 - idade} anos para atingir a maioridade.")
elif idade <= 65:
    print(f"Você é maior de idade. Faltam {65 - idade} anos para atingir 65 anos.")
else:
    print("Você é idoso.")
