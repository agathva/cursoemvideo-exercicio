from random import randint
from time import sleep

print('=='*20)
a = 'JoKenPô'
print(f'{a:^40}')
print('=='*20)

print('Suas opções \n[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura')
jogador = int(input('Qual é sua jogada? '))
computador = randint(1, 3)
print('--'*20)

sleep(1)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
sleep(1)

if jogador == 1:
    if computador == 1:
        print('Empate! \nNós dois escolhemos pedra')
    elif computador == 2:
        print('EU GANHEI! \nEu escolhi papel e você escolheu pedra')
    else:
        print('VOCÊ GANHOU! \nEu escolhi tesoura e você escolheu pedra')
elif jogador == 2:
    if computador == 1:
        print('VOCÊ GANHOU! \nEu escolhi pedra e você escolheu papel')
    elif computador == 2:
        print('Empate! \nNós dois escolhemos papel')
    else:
        print('EU GANHEI! \nEu escolhi tesoura e você escolheu Papel')
elif jogador == 3:
    if computador == 1:
        print('EU GANHEI! \nEu escolhi pedra e você escolheu tesoura')
    elif computador == 2:
        print('VOCÊ GANHOU! \nEu escolhi papel e você escolheu tesoura')
    else:
        print('Empate! \nNós dois escolhemos tesoura')
else:
    print('Opção inválida. Tente novamente')
