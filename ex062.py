termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0

for i in range(1, 11):
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('PAUSA')
print('--' * 35)

while True:
    resposta = int(input('Quantos termos a mais você quer mostar? [0 para não] '))
    if resposta == 0:
        break
    else:
        for i in range(1, resposta+1):
            print(termo, end=' -> ')
            termo += razao
            cont += 1
        print('PAUSA')
print(f'Progressao finalizada com {cont} termos mostrados.')