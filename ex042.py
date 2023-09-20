from math import fabs


print('=='*20)
a = 'ANALISADOR DE TRIÂNGULOS'
print(f'{a:^40}')
print('=='*20)

reta1 = float(input('Segmento da reta 1: '))
reta2 = float(input('Segmento da reta 2: '))
reta3 = float(input('Segmento da reta 3: '))

if fabs(reta2-reta3) < reta1 < reta2 + reta3 or fabs(reta1-reta3) < reta2 < reta1+reta3 or fabs(reta1-reta2) < reta3 < reta1+reta2:
    print('==' * 20)
    if reta1 == reta2 == reta3:
        print('TRIÂNGULO EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('TRIÂNGULO ESCALENO')
    else:
        print('TRIÂNGULO ISÓSCELES')
else:
    print('\nOs segmentos acima não pode formar um triângulo!')
