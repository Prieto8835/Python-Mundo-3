num = tuple(int(input('Write a value : ')) for c in range(1, 5))
print(f'Números digitados: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu pela primeira vez na posição {num.index(3)}')
else:
    print('Não foi digitado nenhum valor 3! ')
cont = 0
print('Números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        cont += 1
        if cont > 0:
            print(n, end=' ')
if cont == 0:
    print('NÃO teve NENHUM número par digitado! ')
