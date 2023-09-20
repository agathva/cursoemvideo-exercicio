qtdd = soma = 0

for i in range(1, 7):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        soma += num
        qtdd += 1

if qtdd != 1:
    print(f'Você informou {qtdd} números PARES e a soma foi {soma}.')
else:
    print(f'Você informou {qtdd} número PAR e a soma foi {soma}.')