valores = list()
for c in range(0, 5):
    x = int(input('Insira um valor: '))
    if c == 0 or x > valores[-1]:
        valores.append(x)
    else:
        pos = 0
        while pos < len(valores):
            if x <= valores[pos]:
                valores.insert(pos, x)
                break
            pos += 1
print('--'*25)
print(f'Valores digitados em ordem foram {valores}')
