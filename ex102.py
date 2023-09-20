def fatorial(número, show=False):
    """
    --> Calcula o fatorial de um número
    :param número: o número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: o valor do fatorial de um número
    """
    fat = 1
    for i in range(número, 0, -1):
        if show == True:
            if i != 1:
                print(i, end= ' * ')
            else:
                print(i, end=' = ')
        fat *= i
    return fat



print(f'{fatorial(5, show = True)}')