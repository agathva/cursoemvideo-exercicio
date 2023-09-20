from datetime import date


anoAtual = date.today().year
maioridade = 0
menoridade = 0

for i in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {i}° pessoa: '))
    idade = anoAtual - nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'{maioridade} pessoas são maiores de idade.')
print(f'{menoridade} pessoas são menores de idade.')
