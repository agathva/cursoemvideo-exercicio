from datetime import date


print('=='*20)
a = 'ANALISANDO ANO BISSEXTO'
print(f'{a:^40}')
print('=='*20)
ano = int(input('Ano [0 analisa o ano atual]: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
