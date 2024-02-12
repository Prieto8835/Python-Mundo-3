valores = ('Zero', 'um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Write a number between 0 and 20: '))
    while num < 0 or num > 20:
        num = int(input('Opção INCORRETA! Por favor digite um número VÁLIDO! (0...20): '))
    print(f'Você escreveu o número: {valores[num]}')
    res = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
    while res != 'Y' and res != 'N':
        res = str(input('Opção INVÁLIDA! Por favor selecione uma CORRETA: [Y/N]: ')).upper().strip()[0]
    if res == 'N':
        print('Its over! ')
        break
