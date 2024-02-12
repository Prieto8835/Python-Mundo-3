n1 = int(input('Write a number: '))
x = input('Escolha uma opção: \n[1 para BINÁRIO] \n[2 para OCTAL] \n[3 para HEXADECIMAL] \nSua opção: ')
if x == '1':
    print('Convertido para BINÁRIO fica:', bin(n1)[2:])
elif x == '2':
    print('Convertido para OCTAL fica:',oct(n1)[2:])
elif x == '3':
    print('Convertido para HEXADECIMAL fica:',hex(n1)[2:])
else:
    print('Opção INCORRETA!')
