expressao = tuple(str(input('Escreva uma expressão: ')))
soma = expressao.count('(') + expressao.count(')')
if soma % 2 == 0:
    print('Válido! ')
else:
    print('Inválido! ')


expr = str(input('Escreva uma expressão: '))
lista = []
for parenteses in expr:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        lista.append(')')
if len(lista) % 2 == 0:
    print('Expressão VÁLIDA! ')
else:
    print('Expressão INVÁLIDA! ')


expr = str(input('Digite uma expressão: '))
lista = []
for parenteses in expr:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Válido ')
else:
    print('Inválido ')
