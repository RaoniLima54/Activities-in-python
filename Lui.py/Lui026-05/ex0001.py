
# 1. Converta metros para quilômetros. Fórmula: km = m / 1000
 
import math

def metros_para_km(m):
    return m/1000

m = int(input('Digite a Número de metros : '))
print(f'{m} metros = {metros_para_km(m)} km')