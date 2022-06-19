import math
from math import hypot

co = int(input('Cateto Oposto: '))
ca = int(input('Cateto Adjacente: '))
hipo = math.hypot(co, ca)
print(f'Hipotenusa: {round(hipo, 2)}')
