# 4. Converta energia de joules para calorias. Fórmula: cal = J / 4.184

import math

def joules_para_calorias(j):
    return j / 4184

j = int(input('Digite o valor em joules :'))
print(f'O valor {j}j = {joules_para_calorias(j)} cal')