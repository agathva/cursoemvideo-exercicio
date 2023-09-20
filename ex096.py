def título(txt):
    print('--' * 10)
    print(txt)
    print('--' * 10)


def área(l, h):
    a = l * h;
    print(f'A área de um terreno {l:.1f}x{h:.1f} é {a:.1f}m²')


#Programa principal
título('CONTROLE DE TERRENO')
largura = float(input("Largura [em metros]: "))
altura = float(input('Altura [em metros]: '))
área(largura, altura)
