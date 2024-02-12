x = y = cont = soma = 0
while x != 999:
    x = int(input(f'{y}° number: '))
    y += 1
    if x == 999:
        cont -= 1
        soma -= x
    cont += 1
    soma += x
print(f'Foram escritos {cont} números e a soma entre eles é {soma}')
