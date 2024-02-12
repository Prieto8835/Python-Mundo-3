from random import randint
num = tuple(randint(0, 10) for c in range(0, 5))
print('Os 5 valores sorteados foram: ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nMaior valor foi: {max(num)} \nMenor valor foi {min(num)}')
