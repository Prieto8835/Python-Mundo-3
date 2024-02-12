from random import randint
cont = 0
while True:
    x = int(input('write a value: '))
    y = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]
    while y != 'P' and y != 'I':
        y = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]
    z = randint(0, 10)
    soma = x + z
    print(f'Você jogou o número {x} e a máquina jogou o número {z}, a soma deu {soma} portanto ', end='')
    if y == 'P':
        if soma % 2 == 0:
            print('deu PAR! Você venceu! ')
            cont += 1
        else:
            print('deu ÍMPAR! Você perdeu! ')
            break
    if y == 'I':
        if soma % 2 == 1:
            print('deu ÍMPAR! Você venceu! ')
            cont += 1
        else:
            print('deu PAR! Você perdeu! ')
            break
print(f'Você ganhou {cont} vezes consecutivas! ')
