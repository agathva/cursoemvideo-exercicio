import math
from math import cos, sin, tan, degrees, radians

angulo = int(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}° tem o SENO de {round(seno, 2)}')
print(f'O ângulo de {angulo}° tem o COSSENO de {round(cosseno, 2)}')
print(f'O ângulo de {angulo}° tem a TANGENTE de {round(tangente, 2)}')
