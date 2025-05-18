def maior_de_tres ( a, b, c):
    return max(a, b, c)
a = int(input('Digite o primeiro número : '))
b = int(input('Digite o segundo número : '))
c = int(input('Digite o terceiro número : '))   

num = maior_de_tres(a, b, c)
print(f'O maior número é :{num}')