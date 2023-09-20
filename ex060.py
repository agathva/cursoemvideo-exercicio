num = int(input('Digite um número: '))

if num > 0:
    c = num
    fatorial = 1
    print(f'{num}! = ', end='')
    while c >= 1:
        print(f'{c} x ' if c>1 else f'{c} ', end='')
        fatorial *= c
        c -= 1
    print(f'= {fatorial}')
elif num == 0:
    print('0! = 1')
else:
    print('Não existe fatorial de número negativo')
