maior = menor = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if peso > maior or i == 1:
        maior = peso
    if peso < menor or i == 1:
        menor = peso

print(f'O maior peso foi {round(maior, 1)}kg.')
print(f'O menor peso foi {round(menor, 1)}kg.')
