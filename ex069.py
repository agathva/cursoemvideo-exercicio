qtdd18 = qtddM = qtddF20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').strip().upper()
    resp = input('Deseja continuar? [S/N] ').strip().upper()
    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N] ').strip().upper()
    if idade > 18:
        qtdd18 += 1
    if sexo == 'M':
        qtddM += 1
    if sexo == 'F' and idade < 20:
        qtddF20 += 1
    if resp == 'N':
        break
print(f'{qtdd18} pessoas tem mais de 18 anos.')
print(f'{qtddM} homens foram cadastrados.')
print(f'{qtddF20} mulheres com menos de 20 anos foram cadastradas.')
