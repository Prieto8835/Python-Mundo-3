med = soma = cont = maior = menor = 0
res = 'Y'
while res == 'Y':
    x = int(input('Write a number: '))
    res = str(input('Quer continuar? [Y/N] ')).upper().strip()[0]
    cont += 1
    soma += x
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
med = soma / cont
print(f'Soma: {soma}, média: {med}, quantidade de valores: {cont}, maior número: {maior}, menor número: {menor}')
