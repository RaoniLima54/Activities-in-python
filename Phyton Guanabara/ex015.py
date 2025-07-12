#Escreva um programa que pergunte a quantidade de km percorridos por carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 

d=int(input('Digite a quantida de dias que o carro será alugado: '))
km=float(input('Digite a quantidade de Quilometros rodados: '))

T = (d * 60) + (km * 0.15) 

print ('O valor a ser pago é R${:.2F}'.format(T))