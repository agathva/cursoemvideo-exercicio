from random import randint


print('-='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*25)

vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    comp = randint(1, 10)
    resultado = jogador + comp
    reps = input('Par ou Impar? [P/I] ').strip().upper()[0]
    while reps not in 'PI':
        reps = input('Par ou Impar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {resultado}')
    if resultado % 2 == 0:
        print('DEU PAR!', end=' ')
        if reps == 'P':
            print('Voce VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif  resultado % 2 != 0 :
        print('DEU ÍMPAR!', end=' ')
        if reps == 'I':
            vitorias += 1
            print('Voce VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('--'*25)
print('--'*25)
print(f'GAMER OVER! Você venceu {vitorias} vez(es).')
