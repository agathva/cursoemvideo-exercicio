num = int(input('Insira um número: '))
div = True

for i in range(2, num):
    if num % i == 0:
        div = False
        break

if div and num > 1:
    print(f'{num} é um número primo')
else:
    print(f'{num} não é um número primo')
