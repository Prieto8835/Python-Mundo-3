x = int(input('[0] Contagem crescente \n[1] Contage descrescente \n[2] Pular de 2 em 2 \n[3] Pular de 3 em 3 \nSua opção: '))
if x == 0:
    for c in range(0, 6):
        print(c)
    print('Chegada')
if x == 1:
    for c in range(5, -1, -1):
        print(c)
    print('Chegada')
if x == 2:
    for c in range(0, 15, 2):
        print(c)
    print('Chegada')
if x == 3:
    for c in range(0, 15, 3):
        print(c)
    print('Chegada')
if x > 3:
    print('Opção INCORRETA!')
y = int(input('Write a number: '))
z = int(input('[0] Ordem crescente \n[1] Ordem decrescente \nSua escolha: '))
if z == 0:
    for c in range(0, y+1):
        print(c)
    print('FIM!!!')
if z == 1:
    for c in range(y, -1, -1):
        print(c)
    print('FIM!!!')
if z > 1:
    print('Escolha INCORRETA!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!!!')
print('--'*20)
print('Soma de valores...')
s = 0
for c in range(0,5):
    n = int(input('Write a number: '))
    s = s + n
print(f'A soma dos valores digitados foi {s}')
