soma = qtdd = 0
while True:
    num = int(input('Insira um numero (999 para parar): '))
    if num == 999:
        break
    soma += num
    qtdd += 1
print(f'A soma dos {qtdd} numeros digitados foi {soma}')
