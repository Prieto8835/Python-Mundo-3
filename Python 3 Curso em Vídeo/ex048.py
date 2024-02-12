print('Números ímpares e múltiplos por 3 entre 1 e 500: ')
for c in range(1, 500):
    if c % 2 == 1:
        if c % 3 == 0:
            print(c)
