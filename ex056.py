maior = somaIdade = menor20F = 0

for i in range(1, 5):
    print(f'{i}° PESSOA')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = int(input('[ 1 ] Feminino \t[ 2 ] Masculino \nSua opção? '))
    somaIdade += idade
    if sexo == 1 and idade < 20:
        menor20F += 1
    if idade > maior and sexo == 2:
        maior = idade
        nomeVelho = nome
    print('--'*20)

media = somaIdade/4
print(f'{round(media, 1)} é média de idade do grupo.')
print(f'O homem mais velho se chama {nomeVelho} e tem {maior} anos.')
print(f'Ao todo são {menor20F} mulheres com menos de 20 anos.')
