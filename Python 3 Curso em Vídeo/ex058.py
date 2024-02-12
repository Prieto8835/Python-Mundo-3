from random import randint
from time import sleep
x = 0
z = 0
y = randint(0, 10)
while x != y:
    print('-'*38)
    x = int(input('Write a value between 0 and 10: '))
    print('Loading...')
    sleep(1)
    if x < y:
        print('Maior...')
    if x > y:
        print('Menor...')
    elif x == y:
        print('Exato!')
    z += 1
print('-'*38)
print(f'I thought about the number {y}')
print(f'Foram necessárias {z} tentativas até acertar!')
