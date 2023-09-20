num = [[], []]
par = list()
impar = list()

for i in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-='*25)
num[0].sort()
num[1].sort()
print(f'O valores pares digitados foram: {num[0]}')
print(f'O valores impares digitados foram: {num[1]}')
