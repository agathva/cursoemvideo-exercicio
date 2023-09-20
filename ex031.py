viagem = float(input('Distância da viagem [km]: '))
if viagem < 200:
    passagem = viagem * 0.50
else:
    passagem = viagem * 0.45
print(f'Você está prestes a começar uma viagem de {viagem}km.')
print(f'Preço da passagem: R${round(passagem, 2):.2f}')
