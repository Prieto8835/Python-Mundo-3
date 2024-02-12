print('Leitura de 6 números inteiros na qual faz a soma apenas dos PARES!')
s = 0
for c in range(6):
    x = int(input('Write a number: '))
    if x % 2 == 0:
        s = s + x
print(f'Resultado da soma dos PARES é: {s}')
