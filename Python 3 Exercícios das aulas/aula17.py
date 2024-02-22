num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #acrescenta o número 7
num[4] = 8
num.sort(reverse=True) #ordem descrescente
num.insert(2, 0) #adiciona na posição 2 o número 0 e reposiciona os demais elementos da lista
num.pop() #remove o último elemento quando () está vazio
num.remove(3) #remove o número 3 da lista
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não tem na lista o número 4 ')
if 5 in num:
    num.remove(5)
    print('Número 5 removido com sucesso de sua lista! ')
print(num)
print(f'Essa lista possui {len(num)} elementos ')

print('-'*30)
valor = []
for cont in range(0, 5):
    valor.append(int(input('Write a value: '))) #adiciona valor escrito pelo usuário a uma lista
valor.append(0)
valor.append(2)
valor.append(4)
print(valor)
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}')

a = [2, 4, 6, 8]
b = a[:] #faz uma cópia dos valores de A
b[2] = 1
print(f'Lista A: {a} ')
print(f'Lista B: {b} ')
