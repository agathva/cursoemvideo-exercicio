from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
print('--'*30)
print('Escolha um número de acordo com a operação desejada: ')
while True:
    menu = int(input('[ 1 ] SOMAR \t[ 2 ] MULTIPLICAR \n[ 3 ] MAIOR \t[ 4 ] NOVOS NÚMEROS \n[ 5 ] SAIR DO PROGRAMA \nSua Opção: '))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        menu = int(input('\033[31mOpção inválida. Tente novamente \033[m'))

    if menu == 1:
        print(f'\033[34mA soma entre {num1} + {num2} = {num1+num2}\033[m')
    elif menu == 2:
        print(f'\033[34mO resultado de {num1} x {num2} = {num1*num2}\033[m')
    elif menu == 3:
        if num1 > num2:
            print(f'\033[34mEntre {num1} e {num2} o maior valor é {num1}\033[m')
        else:
            print(f'\033[34mEntre {num1} e {num2} o maior valor é {num2}\033[m')
    elif menu == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    else:
        print('\033[33mFinalizando a aplicação...\033[m')
        sleep(1)
        break
    print('-=' * 30)
print('=='*25)
print('\033[32mAPLICAÇÃO ENCERRADA COM SUCESSO\033[m')