print('=='*20)
nom = '10 termos de uma PA'
print(f'{nom:^40}')
print('=='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(1, 11):
    print(termo, end=' -> ')
    termo += razao
print('ACABOU')
