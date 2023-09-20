print('=='*20)
nom = '10 termos de uma PA'
print(f'{nom:^40}')
print('=='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1

while c <= 10:
    print(termo, end=' -> ')
    termo += razao
    c += 1
print('FIM')
