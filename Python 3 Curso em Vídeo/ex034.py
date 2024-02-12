x = int(input('Whats is your salary? '))
if x <= 1250:
    print(f'Your new salary is {(x*15/100)+x:.2f}')
else:
    print(f'Your new salary is {(x*10/100)+x:.2f}')
