num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))

print(f'Você digitou os seguintes valores {num}')
print(f'O valor 9 aparece {num.count(9)} vezes.')
if 3 in num:
       print(f'O valor 3 aparece pela primeira vez na posição {num.index(3)}')
else:
       print('Não foi digitado nenhum valor 3')
print('Todos os valores pares digitados', end=' ')
for pos in range(0, len(num)):
       if num[pos] % 2 == 0:
              print(num[pos], end=' ')
