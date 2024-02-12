from random import sample, shuffle #shuffle para sorteio
w = input('Write first name: ')
x = input('Write second name: ')
y = input('Write third name: ')
z = input('Write fourth name: ')
lista = [w, x, y, z]
print('The order of students is:', (sample(lista, 4)))
(shuffle(lista))
print(lista)