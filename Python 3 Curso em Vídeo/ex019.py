from random import choice
w = input('First name: ')
x = input('Second name: ')
y = input('Third name: ')
z = input('Fourth name: ')
lista = [w, x, y, z]
s = choice(lista)
print(f'The winner was: {s}')
