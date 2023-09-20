n = int(input('Quantos termos da Sequência de Fibonacci deseja mostrar? '))
termo1 = 0
termo2 = 1

if n == 1:
    print('0', end=' -> ')
elif n >= 2:
    print('0 -> 1 -> ', end='')
    c = 3
    while c <= n:
        termo3 = termo1 + termo2
        print(f'{termo3} -> ', end='')
        termo1 = termo2
        termo2 = termo3
        c += 1
print('FIM')
