#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h=float(input('Digite a sua altura em metros:'))
s=input('Digite (H) se for homem ou (M) se for mulher:').upper()
if s == 'H':
    pi= (72.7 * h) - 58

elif s == 'M':
    pi= (62.1 * h) - 44.7

else:
    pi=None
    print('Sexo invalidao ,Digite (H) se for homem ou (M) se for mulher:')
    

if pi is not None:
    print('O seu peso ideal é {} kgs'.format(pi))