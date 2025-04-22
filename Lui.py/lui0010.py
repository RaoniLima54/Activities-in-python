#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        #o produto do dobro do primeiro com metade do segundo .
        #a soma do triplo do primeiro com o terceiro.
        #o terceiro elevado ao cubo.

n1=int(input('Digite o primeito numero inteiro:'))
n2=int(input('Digite o segundo número inteiro:'))
n3=float(input('Digite o terceiro número , agora real :'))
p1=(n1*2)*(n2/2)
p2=(n1*3)+ n3
p3=n3**3
print('O valor do produto do dobro do {} com a metade do {} é {}'.format(n1,n2,p1))
print('A soma do triplo de {} com {} é {}'.format(n1,n3,p2))
print('O valor do cubo de {} é {}'.format(n3,p3))