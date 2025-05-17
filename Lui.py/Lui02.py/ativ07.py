#Peça ao usuário um número inteiro e exiba todos os números de 1 a 100 que são divisíveis por esse número, juntamente com a contagem total de números divisíveis encontrados. 
numero = int(input("Digite um número inteiro: "))

divisiveis = [i for i in range(1, 101) if i % numero == 0]

print("Números divisíveis por", numero, "de 1 a 100:", divisiveis)
print("Quantidade total de números encontrados:", len(divisiveis))
