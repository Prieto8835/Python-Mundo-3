old = 0
oldname = ''
totidade = 0
totm = 0
m20 = 0
med = 0
for c in range(1, 5):
    print('-'*5, f'{c}° PESSOA', '-'*5)
    nome = str(input('Whats your name? '))
    idade = int(input('How old are you? '))
    sexo = str(input('Qual seu gênero? [M/F] ')).upper().strip()
    totidade = totidade + idade
    med = totidade/4
    print('-' * 35)
    if sexo == 'M':
        totm = totm + 1
        if c == 1:
            old = idade
            oldname = nome
        if idade > old:
            old = idade
            oldname = nome
    if sexo == 'F':
        if idade < 20:
            m20 = m20 + 1
if m20 == 0:
    print('Não existem mulheres no grupo')
if m20 >= 1:
    print(f'Tem {m20} mulheres com menos de 20 anos no grupo')
if totm == 0:
    print('Não existem homens no grupo')
if totm >= 1:
    print(f'O Homem mais velho do grupo tem {old} anos e se chama {oldname.strip()}')
print(f'A média de idade do grupo é {med} anos')
