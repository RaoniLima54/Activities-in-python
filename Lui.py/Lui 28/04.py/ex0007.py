#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    custo_final = custo + (custo * (taxaImposto / 100))
    return custo_final

taxa = float(input("Digite a taxa de imposto (em %): "))
custo_original = float(input("Digite o custo do item: R$ "))

custo_com_imposto = somaImposto(taxa, custo_original)

print(f"\nCusto original: R${custo_original:.2f}")
print(f"Custo com imposto de {taxa}%: R${custo_com_imposto:.2f}")
