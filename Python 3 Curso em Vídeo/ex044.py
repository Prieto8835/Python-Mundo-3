x = float(input('Valor do produto: R$ '))
y = int(input('Qual condição de pagamento? \n[1] À vista dinheiro/cheque \n[2] À vista no cartão \n[3] Até 2x no cartão \n[4] 3x ou mais no cartão \nSua opção: '))
vista = x-(x*10)/100
vistaC = x-(x*5)/100
cartao3x = x+(x*20)/100
if y == 1:
    print(f'Com pagamento à vista no dinheiro/cheque o preço final com 10% de desconto fica: R${vista:.2f}')
elif y == 2:
    print(f'Com pagamento à vista no cartão o preço final com 5% de desconto fica: R${vistaC:.2f}')
elif y == 3:
    print(f'Com pagamento em até 2x no cartão o preço final fica: R${x:.2f}')
    print(f'Sendo parcelada em 2x de R${x/2:.2f}')
elif y == 4:
    z = int(input('Quantas parcelas? '))
    print(f'Com pagamento no cartão em 3x ou mais o preço final com acréscimo de 20% fica: R${cartao3x:.2f}')
    print(f'Sendo parcelada em {z}x de R${cartao3x/z:.2f}')
else:
    print('Opção INCORRETA!')
