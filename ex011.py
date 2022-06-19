alt = float(input('Altura da parede [em metros]: '))
larg = float(input('Largura da parede [em metros]: '))
área = alt * larg
tinta = área / 2
print(f'Sua parece tem a dimensão {alt}x{larg} e sua área é de {round(área, 2)}m²')
print(f'Para pintar essa parede, você precisará de {round(tinta)}L de tinta')
