def ficha(nome='<desconhecido>', gols= '0'):
    if nome.strip() == '' or gols.strip() == '':
        nome = '<desconhecido>'
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome: '))
gol = str(input('Quantidade de gols marcado: '))
print('--'*25)
ficha(nome, gol)
