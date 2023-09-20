nome = input('Digite seu nome completo: ').strip().title()

print('=='*25)
print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é {nome.upper()}.')
print(f'Seu nome em minúsculo é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro tem {nome.find(" ")} letras.')
print('=='*25)
