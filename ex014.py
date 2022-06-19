c = float(input('Insira uma temperatura [em °C]: '))
f = 9 * c / 5 + 32
k = c + 273.15
print(f'{round(c, 2)}°C = {round(f, 2)}°F = {round(k, 2)}K')
