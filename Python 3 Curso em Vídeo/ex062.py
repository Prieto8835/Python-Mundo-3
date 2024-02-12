print('-'*75)
print('10 primeiros termos de uma P.A com opção de continuação pelo usuário!')
x = int(input('Escreva o número inicial: '))
y = int(input('Escreva a razão da P.A: '))
z = 0
print(x, end=' > ')
while z != 9:
    x += y
    print(x, end=' > ')
    z += 1
print('Its over')
cont = str(input('Do you want to continue? [Y/N] ')).upper().strip()
while cont != 'N' and cont != 'Y':
    cont = str(input('Escolha uma opção correta [Y/N] ')).upper().strip()
while cont == 'Y':
    newpa = int(input('Escreva a nova razão da P.A: '))
    term = int(input('Quantos termos quer somar: '))
    print(x, end=' > ')
    z = 0
    while z != term:
        x += newpa
        print(x, end=' > ')
        z += 1
    print('Its over')
    cont = str(input('Do you want to continue? [Y/N] ')).upper().strip()
    while cont != 'N' and cont != 'Y':
        cont = str(input('Escolha uma opção correta [Y/N] ')).upper().strip()
if cont == 'N':
    print('Its over')
