#8. :
#Crie um programa que gere e exiba todos os números da sequência de Fibonacci até um valor n fornecido pelo usuário. Pergunte ao usuário qua((l o limite máximo para a sequência :


def fibonacci_sequenci(limit):
    fib = [0, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > limit:
            break
        fib.append(next_fib)
    return fib



n=int(input('Digite o valor máximo para seguencia de Fibonacci: ')) 
R = fibonacci_sequenci(n)
print('Sequência de Fibonnaci até',n,':' ,R)