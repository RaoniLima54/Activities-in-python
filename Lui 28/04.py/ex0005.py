
# Crie um programa que tenha uma função fatorial() e retorno o valor fatorial de três variáveis em tela.

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

a = 5
b = 3
c = 7


fatorial_a = fatorial(a)
fatorial_b = fatorial(b)
fatorial_c = fatorial(c)


print(f"O fatorial de {a} é {fatorial_a}")
print(f"O fatorial de {b} é {fatorial_b}")
print(f"O fatorial de {c} é {fatorial_c}")
