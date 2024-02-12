"""a = float(input('Qual seu peso? '))
b = float(input('Qual seu peso? '))
c = float(input('Qual seu peso? '))
d = float(input('Qual seu peso? '))
e = float(input('Qual seu peso? '))
if e > d and e > c and e > b and e > a:
    print(f'Maior {e}')
elif d > e and d > c and d > b and d > a:
    print(f'Maior {d}')
elif c > e and c > d and c > b and c > a:
    print(f'Maior {c}')
elif b > e and b > d and b > c and b > a:
    print(f'Maior {b}')
else:
    print(f'Maior {a}')
if e < d and e < c and e < b and e < a:
    print(f'Menor {e}')
elif d < e and d < c and d < b and d < a:
    print(f'Menor {d}')
elif c < e and c < d and c < b and c < a:
    print(f'Menor {c}')
elif b < e and b < d and b < c and b < a:
    print(f'Menor {b}')
else:
    print(f'Menor {a}')"""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual seu peso? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Mais pesado: {maior}')
print(f'Mais leve: {menor}')
