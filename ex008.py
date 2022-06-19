metros = float(input('Insira uma distância [em metros]: '))
cm = metros * 100
mm = metros * 1000

print('=='*20)
print(f'{metros/1000}km.')
print(f'{metros/100}hm.')
print(f'{metros/10}dam')
print(f'{metros}m')
print(f'{metros*10}dm')
print(f'{metros*100}cm')
print(f'{metros*1000}mm')
print('=='*20)