# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo reângulo, calcule e mostre o comprimento da hipotenusa. 

CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))

#hi = (CA**2) + (CO**2) ** (1/2)
#print('A hiportenusa vai medir{}'.format(hi))



import math 
hi = math.hypot(CA , CO)
print('A hipotenusa vai medir{:.2f}'.format(hi))