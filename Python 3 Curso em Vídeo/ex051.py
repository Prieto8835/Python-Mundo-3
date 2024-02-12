print('10 primeiros números de uma P.A: ')
x = int(input('Escreva o número inicial: '))
y = int(input('Escreva a razão da P.A: ')) #sequência de números onde a diferença entre dois termos consecutivos é sempre a mesma
print(x)
for c in range(9):
    x = x + y
    print(x)
print('Acabou!!!')
