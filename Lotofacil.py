import random

# Função para garantir que o número de dezenas seja válido (entre 15 e 18)
def obter_qtd_dezenas():
    while True:
        try:
            qtd = int(input("Quantas dezenas você deseja marcar (entre 15 e 18): "))
            if 15 <= qtd <= 18:
                return qtd
            else:
                print("Quantidade de dezenas inválida. Digite um valor entre 15 e 18.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Função para obter os números da aposta
def obter_dezenas(qtd_dezenas):
    dezenas = set()
    while len(dezenas) < qtd_dezenas:
        try:
            dezena = int(input(f"Digite o {len(dezenas)+1}º número (entre 1 e 25): "))
            if dezena < 1 or dezena > 25:
                print("Dezena inválida. O número deve estar entre 01 e 25.")
            elif dezena in dezenas:
                print("Número repetido. Digite um número diferente.")
            else:
                dezenas.add(dezena)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    return sorted(dezenas)

# Função para gerar uma aposta surpresinha (18 números)
def gerar_aposta_surpresa():
    return sorted(random.sample(range(1, 26), 18))

# Função para gerar o resultado do concurso (15 números sorteados)
def gerar_resultado_concurso():
    return sorted(random.sample(range(1, 26), 15))

# Função principal
def main():
    # Etapa a: Solicitar a quantidade de dezenas
    qtd_dezenas = obter_qtd_dezenas()
    
    # Etapa b: Solicitar os números da aposta
    aposta_usuario = obter_dezenas(qtd_dezenas)
    
    # Etapa c: Gerar duas apostas surpresinha
    aposta_surpresinha1 = gerar_aposta_surpresa()
    aposta_surpresinha2 = gerar_aposta_surpresa()
    
    # Etapa d: Gerar o resultado do concurso
    resultado_concurso = gerar_resultado_concurso()
    
    # Etapa e: Imprimir os resultados em ordem crescente
    print("\nSua aposta:")
    print(aposta_usuario)
    
    print("\nAposta Surpresinha 1:")
    print(aposta_surpresinha1)
    
    print("\nAposta Surpresinha 2:")
    print(aposta_surpresinha2)
    
    print("\nResultado do Concurso Lotofácil:")
    print(resultado_concurso)

# Executar o programa
if __name__ == "__main__":
    main()
