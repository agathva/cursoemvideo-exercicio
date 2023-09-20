frase = input('Digite uma frase: ').upper().strip()
junto = ''.join(frase.split())
palindromo = True

for i in range(0, len(junto)):
    if junto[i] != junto[len(junto)-1-i]:
        palindromo = False
        break

if palindromo:
    print(f'{frase} é um palíndromo')
else:
    print(f'{frase} não é um palíndromo')
