# 5. Converta horas para segundos. Fórmula: s = h * 3600

import math

def hora_para_segundos(h):
    return h * 3600

h = int(input('Digite as horas : '))
print(f'As {h} horas = {hora_para_segundos(h)} segundos')