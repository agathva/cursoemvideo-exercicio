print('=='*25)
a = 'SISTEMA DE CONVERSÃO DE BASES'
print(f'{a:^50}')
print('=='*25)

decimal = int(input('Digite um número inteiro: : '))
print('Escolha uma das bases para conversão \n[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal')
escolha = int(input(f'Sua opção: '))
print('=='*25)

if escolha == 1:
    print(f'{decimal} convertido para binário é igual a {bin(decimal)[2:]}')
elif escolha == 2:
    print(f'{decimal} convertido para octal é igual a {oct(decimal)[2:]}')
elif escolha == 3:
    print(f'{decimal} convertido para hexadecimal é igual a {hex(decimal)[2:]}')
else:
    print('Opção inválida. Tente novamente')
