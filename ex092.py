from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
pessoa['idade'] = anoAtual - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário R$: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35 - anoAtual)
print(pessoa)
print('=='*25)

for k, v in pessoa.items():
    print(f'{k} tem o valor de {v}')
