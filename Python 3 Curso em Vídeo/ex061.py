print('Escreva os 10 primeiros números de uma P.A: ')
x = int(input('Número inicial: '))
y = int(input('Razão da P.A: '))
z = 0
print(x, end=' > ')
while z != 9:
    x = x + y
    print(x, end=' > ')
    z += 1
print('Its over')
