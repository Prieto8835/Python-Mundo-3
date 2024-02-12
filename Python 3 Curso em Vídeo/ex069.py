maior = homens = mulher = 0
while True:
    idade = int(input('How old are you? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    res = str(input('Do you to continue? [Y/N] ')).upper().strip()[0]
    while res != 'Y' and res != 'N':
        res = str(input('Do you to continue? [Y/N] ')).upper().strip()[0]
    print('-~'*30)
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    if res == 'N':
        break
print(f'Tem {maior} pessoas acima dos 18 anos; {homens} homens cadastrados e {mulher} mulheres com menos de 20 anos cadastradas! ')
