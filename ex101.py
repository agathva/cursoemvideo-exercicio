def voto(nascimento):
    """
    função que calcula a idade de uma pessoa a partir do ano de nascimento e mostra se o voto é NEGADO, OBRIGATÓRIO ou OPCIONAL de acordo com a idade
    :param nascimento: recebe como parâmetro o ano de nascimento
    :return: sem retorno
    """
    from datetime import date


    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    elif 16 >= idade or idade < 18 or idade > 70:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')


nasc = int(input('Digite o ano de nascimento: '))
voto(nasc)
