#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


def verifica_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

n1 = 10
n2 = 0
n3 = -5

print(f"{n1}: {verifica_sinal(n1)}")
print(f"{n2}: {verifica_sinal(n2)}")
print(f"{n3}: {verifica_sinal(n3)}")
