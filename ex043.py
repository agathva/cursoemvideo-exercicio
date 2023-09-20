peso = float(input('Peso (kg): '))
altura = float(input('Altura (metros): '))
imc = peso/altura**2
print(f'IMC: {round(imc, 1)}')

if imc < 18.5:
    print('Você está em ABAIXO DO PESO')
elif imc <= 25:
    print('Parabéns, você está em um PESO NORMAL')
elif imc <= 30:
    print('Você está em SOBREPESO')
elif imc <= 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
