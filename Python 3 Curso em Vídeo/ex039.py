from datetime import date
z = str(input('Qual seu sexo? \n[M] Masculino \n[F] Feminino \nSua opção: ')).upper()
y = date.today().year
x = int(input('Ano de nascimento: '))
if z == 'M':
    if y - x < 18:
        print(f'Nascido em {x}, você tem {y-x} anos e faltam {18-(y-x)} anos para seu alistamento. Ano de alistamento será {x+18}')
    elif y - x == 18:
        print(f'Nascido em {x}, você tem {y-x} anos e nesse ano de {y} está na hora de se alistar')
    elif y - x > 18:
        print(f'Nascido em {x}, você tem {y-x} anos e se alistou faz {(y-x)-18} anos. Sendo o ano de alistamento {x+18}')
else:
    print('Por ser do sexo feminino, não há necessidade de alistamento')
