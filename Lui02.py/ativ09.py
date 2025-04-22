
#9.:
#Escolha um número aleatório entre 1 e 100. Peça ao usuário para adivinhar o número e informe se o palpite é muito alto, muito baixo ou correto. Permita que o usuário continue tentando até adivinhar corretamente. Adicione um contador para mostrar quantas tentativas foram feitas.  

import random

def jogo_adivinhacao():
    N = random.randint(1,100)
    T = 0

    print ('Tente adivinha um número de 1 a 100!')

    while True:
        try:
            D=int(input('Digite seu palpite: '))
            T +=1

            if D < N :
                print('Muito baixo , tente de novo!')

            elif D > N :
                print('Muito alto , tente de novo!')

            else:
                print ('Parabéns! Você aceitou em {} tentativas.'.format(T))
                break
        except ValueError:
            print('Insirá um valor válido.')
jogo_adivinhacao()