from datetime import date


nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {anoAtual}')

if idade > 18:
    print(f'Já se passaram {idade-18} anos para alistamento militar.')
    print(f'Seu alistamento foi em {anoAtual-(idade-18)}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Ainda falta(m) {18-idade} anos para o alistamento militar.')
    print(f'Seu alistamento será em {anoAtual+(18-idade)}')
