soma = cont = 0
while True:
    x = int(input('Write a number: '))
    if x == 999:
        break
    soma += x
    cont += 1
print(f'A soma dos {cont} valores é {soma}')
