x = float(input(f'Qual sua altura? (m) '))
y = float(input('Qual seu peso? (kg) '))
imc = y/x**2
print(f'Seu IMC é de {imc:.2f} e segundo essa informação: ')
if imc < 18.5:
    print('MAGREZA!')
elif 18.5 < imc < 24.9:
    print('NORMAL!')
elif 25 < imc < 29.9:
    print('SOBREPESO!')
elif 30 < imc < 34.9:
    print('OBESIDADE GRAU I!')
elif 35 < imc < 39.9:
    print('OBESIDADE GRAU II!')
else:
    print('OBESIDADE GRAU III!')
