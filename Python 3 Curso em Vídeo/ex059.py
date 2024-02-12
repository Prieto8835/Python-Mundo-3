from time import sleep
a = int(input('Write first value: '))
b = int(input('Write second value: '))
c = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Digitar novos números \n[5] Sair do programa \nSua opção: '))
while c != 5:
    if c > 5:
        print('Opção inválida! Por favor selecione uma opção correta! ')
    if c == 4:
        a = int(input('Write first value: '))
        b = int(input('Write second value: '))
        c = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Digitar novos números \n[5] Sair do programa \nSua opção: '))
    if c == 1:
        soma = a + b
        print(f'A soma entre {a} e {b} é {soma}')
    if c == 2:
        mult = a * b
        print(f'A multiplicação entre {a} e {b} é {mult}')
    if c == 3:
        if a > b:
            print(f'O maior valorentre {a} e {b} é {a}')
        else:
            print(f'O maior valor entre {a} e {b} é {b}')
    c = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior número \n[4] Digitar novos números \n[5] Sair do programa \nSua opção: '))
if c == 5:
    print('Saindo...')
    sleep(1)
    print('Obrigado pela preferência, volte sempre!')
