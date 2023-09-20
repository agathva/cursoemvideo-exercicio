def maior(*valores):
    from time import sleep

    print('Analisando os valores passados...')
    for i in range(0, len(valores)):
        print(valores[i], end= ' ')
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')

    maior = 0
    for i in range(0, len(valores)):
        if (i == 0 or valores[i] > maior):
            maior = valores[i]
    print(f'O maior valor informado foi {maior}')
    print('-='*25)
    sleep(0.2)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(1, 90, 6, 19)
maior(6)
maior()
