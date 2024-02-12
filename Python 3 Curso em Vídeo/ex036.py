casa = float(input('Qual valor da casa? '))
salário = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos vai pagar? '))
x = (casa/anos)/12 #valor da parcela
y = (30*salário)/100 #30% do salário
print(f'Valor da parcela: {x:.2f}')
print(f'Valor correspondente a 30% do salário: {y:.2f}')
if x <= y:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')