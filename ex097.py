def mensagem(txt):
    tam = len(txt) + 6
    print('-'*(tam))
    print(f'{txt:^{(tam)}}')
    print('-' * (tam))

msm = str(input('Escreva uma mensagem: '))
mensagem(msm)
