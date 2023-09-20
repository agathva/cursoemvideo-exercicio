def sorteia(números):
    from random import randint
    from time import sleep

    print('Sorteando 5 valores da lista: ', end=' ')
    for i in range(0, 5):
        números.append(randint(1, 10))
        print(números[i], end=' ')
        sleep(0.5)
    print('PRONTO!')

def somaPar(números):
    soma = 0
    for i in range(0, 5):
        if números[i] % 2 == 0:
            soma += números[i]
    print(f'Somando os valores pares de {números}, temos {soma}.')


números = list()
sorteia(números)
somaPar(números)
