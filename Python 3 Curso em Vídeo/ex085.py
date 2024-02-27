num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
print(f'Números pares são {sorted(num[0])}')
print(f'Números ímpares são {sorted(num[1])}')
