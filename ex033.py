num1 = int(input('1° número: '))
num2 = int(input('2° número: '))
num3 = int(input('3° número: '))

# Achar o menor valor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Achar o maior valor
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num1:
    maior = num3
print(f'maior número é {maior} e o menor é {menor}')
