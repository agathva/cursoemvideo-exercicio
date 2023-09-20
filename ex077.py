'''cores = ('azul', 'verde', 'amarelo', 'roxo', 'rosa', 'vermelho', 'laranja', 'marrom', 'cinza', 'branco', 'preto')
for pos, cor in enumerate(cores):
    print(f'Na palavra {cor.upper()} temos', end=' ')
    if 'A' in cor.upper():
        print('A', end=' ')
    if 'E' in cor.upper():
        print('E', end=' ')
    if 'I' in cor.upper():
        print('I', end=' ')
    if 'O' in cor.upper():
        print('O', end=' ')
    if 'U' in cor.upper():
        print('U', end=' ')
    print()'''

vogais = ('a', 'e', 'i', 'o', 'U')
cores = ('azul', 'verde', 'amarelo', 'roxo', 'rosa', 'vermelho', 'laranja', 'marrom', 'cinza', 'branco', 'preto')
for cor in cores:
    print(f'Na palavra {cor.upper()} temos', end=' ')
    for letras in cor:
        if (letras.lower() in vogais):
            print(f'{letras.lower()}', end=' ')
    print()
