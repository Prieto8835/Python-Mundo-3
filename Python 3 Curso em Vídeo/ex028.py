from random import choice, randint
from time import sleep #sleep para fazer com que espere
x = int(input('Write a value between 0 and 5: '))
z = randint(0, 5)
#y = [0, 1, 2, 3, 4, 5]
#z = choice(y)
print('Loading...')
sleep(3) #esperar 3 segundos
print(f'I thought about the number: {z}')
if x == z:
    print('You win!')
else:
    print('You Lose!')
