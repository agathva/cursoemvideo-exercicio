def contador(início, fim, passo):
    from time import sleep

    if passo == 0:
        passo = 1
    print(f'Contagem de {início} até {fim} de {abs(passo)} em {abs(passo)}')
    if (início > fim or passo < 0 and início > fim):
            for i in range(início, fim-1, -abs(passo)):
                print(i, end=' ', flush=True)
                sleep(0.5)
    elif (início < fim and passo > 0):
        for i in range(início, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    else:
        print("ERRO, CONTAGEM INCOERENTE!")
    print('FIM')
    print('-='*20)


contador(1, 10, 1)
contador(10, 1, 1)

print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-='*20)
contador(início, fim, passo)
