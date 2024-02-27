grupo = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso em kg: ')))
    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    grupo.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while res != 'S' and res != 'N':
        res = str(input('Resposta errada, escolha uma VÁLIDA [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
print(f'Quantidade de pessoas cadastradas foram {len(grupo)} ')
print(f'Menor peso foi {menor} da(s) pessoa(s) ', end='')
for nome, peso in grupo:
    if peso == menor:
        print(f'{[nome]}', end='')
print()
print(f'Maior peso foi {maior} da(s) pessoa(s) ', end='')
for nome, peso in grupo:
    if peso == maior:
        print(f'{[nome]}', end='')
