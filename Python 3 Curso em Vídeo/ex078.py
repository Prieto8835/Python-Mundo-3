num = []
for cont in range(0, 5):
    num.append(int(input('Write a number: ')))
print(f'Valores armazenados na lista são: {num}')
print(f'Maior valor da lista é {max(num)} e está na(s) posição(ões) ', end='')
for pos, valor in enumerate(num):
    if valor == max(num):
        print(f'{pos}...', end='')
print(f'\nMenor valor da lista é {min(num)} e está na(s) posição(ões) ', end='')
for pos, valor in enumerate(num):
    if valor == min(num):
        print(f'{pos}...', end='')
print()
