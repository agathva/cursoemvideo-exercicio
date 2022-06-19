import socket
nome = input('Digite seu nome: ')
print(f'É um prazer te conhecer, {nome}! \nEu sou {socket.gethostname()}')
