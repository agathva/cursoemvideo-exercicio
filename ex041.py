from datetime import date


nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade <= 20:
    print('CATEGORIA SENIOR')
else:
    print('CATEGORIA MASTER')
