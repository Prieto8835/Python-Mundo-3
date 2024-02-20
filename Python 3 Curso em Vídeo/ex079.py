num = []
while True:
    x = int(input('Write a value: '))
    if x not in num:
        num.append(x)
    else:
        print('Valor já adicionado, não vou adicioná-lo novamente! ')
    res = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
    while res != 'Y' and res != 'N':
        res = str(input('Resposta INVÁLIDA! Por favor escolha uma correta! [Y/N] ')).upper().strip()[0]
    if res == 'N':
        break
print(f'Números digitados foram {num}')
print(f'Em ordem crescente fica {sorted(num)}')
