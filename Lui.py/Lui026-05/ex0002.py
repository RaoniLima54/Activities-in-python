# 2. Converta Celsius para Fahrenheit. Fórmula: F = (C * 9/5) + 32

import math

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


c = int(input('Digite a temperatura a ser covertida de celsisus para fahrenheit: '))
print (f'A temperatura{c} convertida é {celsius_para_fahrenheit(c)}')