#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaParz(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random

def sorteia(lista):
    print('Sorteando 5 números para a lista: ', end='')
    for _ in range(5):
        num = random.randint(1, 10)
        lista.append(num)
        print(num, end=' ', flush=True)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"Somando os valores pares de {lista}, temos {soma}.")


números = []
sorteia(números)
somaPar(números)
