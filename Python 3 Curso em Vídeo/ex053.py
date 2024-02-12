print('Leitura para identificar se uma frase é políndromo, ou seja, permanece igual quando lida de trás pra frente')
x = str(input('Escreva uma frase: ')).replace(' ', '')
print(x)
print(x[::-1])
if x == x[::-1]:
    print('Políndromo')
else:
    print('Não políndromo')
