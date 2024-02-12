x = int(input('How far is the trip? '))
if x <= 200:
    print(f'The ticket price is R${0.5*x:.2f}')
else:
    print(f'The ticket price is R${0.45*x:.2f}')
