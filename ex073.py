colocação = ('Palmeiras', 'Flamengo', 'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Santos', 'Bragantino', 'Goiás', 'Fortaleza', 'Botafogo', 'São Paulo', 'Ceará SC', 'Cuiabá', 'Coritiba', 'Avaí', 'Atlético-GO', 'Juventude')
print(f'Lista dos times do Brasileirão {colocação}')
print(f'Os cinco primeiros colocados são {colocação[:5]}')
print(f'Os quatro últimos colocados são {colocação[-4:]}')
print(f'Times em ordem alfabética: {sorted(colocação)}')
if 'Chapecoense' in colocação == False:
    print('Chapecoense não conseguiu se classificar')
else:
    print(f'O Chapecoense esta na {colocação.index("Chapeconse")+1}ª posição')
