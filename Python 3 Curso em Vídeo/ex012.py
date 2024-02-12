x = float(input('Whats is the price of the product? '))
y = float(input('Whats is the discount percentage? '))
#a = (x*y)/100
#b = x-y
#print(f'Valor com desconto: {b}')
print(f'Value with discount: R${x-(x*y)/100:.2f}')
#print(f'Com desconto de 5% fica {(x*5)/100}')
