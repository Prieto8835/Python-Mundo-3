num = list()
while True:
    num.append(int(input('Write a number: ')))
    res = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
    while res != 'Y' and res != 'N':
        res = str(input('Opção INVÁLIDA! [Y/N] ')).upper().strip()[0]
    if res == 'N':
        break
numpar = list()
numimpar = list()
for par in num:
    if par % 2 == 0:
        numpar.append(par)
for impar in num:
    if impar % 2 == 1:
        numimpar.append(impar)
print(f'Lista com números pares: {numpar} \nLista com números ímpares: {numimpar} \nLista original: {num} ')
