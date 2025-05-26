#3. Converta m/s para km/h. Fórmula: km/h = m/s * 3.6
import math

def ms_para_kmh(ms):
    return ms * 3.6

ms = int(input(('Digite a velocidade em metros por segundo : ')))
print(f'A velocidade {ms} convetida é {ms_para_kmh(ms):.0f} km/h')