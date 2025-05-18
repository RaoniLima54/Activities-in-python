def convert_temperatura(C):
    F = (C*9/5)+32
    return F
C = int(input('Digite a temperatura em graus Celsius:'))

f=convert_temperatura(C)
print(f'A temperatura em Fahrenheit:{f}°F')