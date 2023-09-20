qtdd = soma = 0

while True:
    num = int(input('Insira um número [999 para parar]: '))
    if num == 999:
        break
    else:
        soma += num
        qtdd += 1
print(f'A soma de todos os {qtdd} números digitados é igual a {soma}.')