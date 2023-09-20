def leiaInt(valor):
    while valor.isnumeric() != True:
        valor = str(input('ERRO, Digite um valor numérico! '))
    return valor


n = leiaInt(input('Digite um valor: '))
print(f'Você acabou de digitar o número {n}')