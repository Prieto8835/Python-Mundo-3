tot = mais = caro = barato = cont = 0
nomecaro = nomebarato = ''
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$ '))
    res = str(input('Do you to continue? [Y/N] ')).upper().strip()[0]
    while res != 'Y' and res != 'N':
        res = str(input('Do you to continue? [Y/N] ')).upper().strip()[0]
    print('-~'*20)
    tot += valor
    cont += 1
    if valor > 1000:
        mais += 1
    if cont == 1 or valor < barato:
        barato = valor
        nomebarato = nome
    if valor > caro:
        caro = valor
        nomecaro = nome
    if res == 'N':
        break
print(f'Valor total gasto na compra é R$ {tot:.2f} \nExistem {mais} produtos acima dos R$ 1000.00')
print(f'O produto mais caro é {nomecaro} e custa R${caro:.2f}')
print(f'O produto mais barato é {nomebarato} e custa R${barato:.2f}')
