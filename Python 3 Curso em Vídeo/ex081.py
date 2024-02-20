num = []
while True:
    num.append(int(input('Escreva um número: ')))
    res = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while res != 'S' and res != 'N':
        res = str(input('Opção ERRADA! Selecione uma disponível: [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
print(f'Números armazenados na lista são: {num} ')
print(f'Ao total foram digitados {len(num)} valores ')
num.sort(reverse=True)
print(f'Lista de valores em ordem decrescente fica {num}')
if 5 in num:
    print('O valor 5 FOI digitado e está na lista! ')
else:
    print('O valor 5 NÃO foi digitado e não está na lista! ')
