vel = float(input('Velocida do carro [km/h]: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[0;31mVocê excedeu a velocidade limite de 90km/h!')
    print(f'Multado em R${round(multa, 2):.2f}\033[m')
print('\033[0;33mTenha um bom dia! Dirija com segurança!')
