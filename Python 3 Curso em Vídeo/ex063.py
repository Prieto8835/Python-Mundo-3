x = int(input('Write a number: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} > {t2}', end=' > ')
while x >= cont:
    t3 = t1 + t2
    cont += 1
    print(t3, end=' > ')
    t1 = t2
    t2 = t3
print('Finish')
