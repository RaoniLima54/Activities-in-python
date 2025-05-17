#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: de 1 até 10, de 1 em 1;  de 10 até 0, de 2 em 2

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo
        
    print('-' * 30)

    print(f"Contando de {inicio} até {fim} de {passo} em {passo}")
    sleep(1)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= passo
    print("FIM!")
    print('-' * 30)

contador(1, 10, 1)
contador(10, 0, 2)


