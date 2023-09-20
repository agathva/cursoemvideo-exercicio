aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: ')).strip().title()
aluno['Média'] = float(input(f'Media de  {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
else:
    aluno['Situação'] = 'EM RECUPERAÇÃO'

print('--'*25)
for k, v in aluno.items():
    print(f'{k}: {v}')
