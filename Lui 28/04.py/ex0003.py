#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* números):
    print('-' * 30)
    print('Analisando os valores passados...')
    for num in números:
        print(num, end=' ', flush=True)
        sleep(0.3)
    print(f"\nForam informados {len(números)} valores ao todo.")
    
    if len(números) == 0:
        print("Nenhum valor foi informado.")
    else:
        maior = números[0]
        for num in números:
            if num > maior:
                maior = num
        print(f"O maior valor informado foi {maior}.")
    print('-' * 30)


valores = [] 

print("Digite os valores. Quando quiser parar, digite 'fim'.")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'fim':
        break
    if entrada.isnumeric() or (entrada[0] == '-' and entrada[1:].isnumeric()):
        valores.append(int(entrada))
    else:
        print("Valor inválido. Digite um número inteiro ou 'fim' para encerrar.")


maior(*valores)

