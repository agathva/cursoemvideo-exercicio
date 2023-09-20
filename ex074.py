from random import randint

sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os números', end=' ')
for numero in sorteados:
    print(numero, end=' ')
print(f'O maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')
