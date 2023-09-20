nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print(f'REPROVADO com média {round(media, 1):.1f}')
elif media < 7:
    print(f'RECUPERAÇÃO com média {round(media, 1):.1f}')
else:
    print(f'APROVADO com média {round(media, 1):.1f}')
