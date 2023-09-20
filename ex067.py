while True:
    num = int(input('Quer ver a tabuada de qual valor? [negativo para parar] '))
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num} x {c:>2} = {(num*c):>3}')
    print('==' * 25)
print('FIM')
