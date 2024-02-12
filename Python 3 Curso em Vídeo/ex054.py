from datetime import date
year = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    x = int(input('Qual seu ano de nascimento? '))
    if (year - x) > 21:
        maior = maior + 1
    elif (year - x) <= 21:
        menor = menor + 1
print(f'A quantidade de menores de idade (considerando 21 anos) são {menor}')
print(f'A quantida de maiores de idade (considerando 21 anos) são {maior}')
