expressão = str(input('Digite a expressão: '))
aberto = expressão.count('(')
fechado = expressão.count(')')
if expressão.index(')') > expressão.index('('):
    if aberto == fechado:
        print('Expressão válida')
    else:
        print('Expressão é inválida')
else:
    print('Expressão inválida')
