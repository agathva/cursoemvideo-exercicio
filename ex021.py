from pygame import mixer
mixer.init() #Iniciar a biblioteca PyGame
mixer.music.load('ex021.mp3') #Carregar o arquivo MP3
mixer.music.play() #iniciar o arquivo MP3

input('Aperte ENTER para parar')
