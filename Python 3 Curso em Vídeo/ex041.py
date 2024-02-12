from datetime import date
x = date.today().year
year = int(input('Que ano você nasceu? '))
y = x-year
print(f'{y} years')
if y <= 9:
    print('MIRIM')
elif y <= 14:
    print('INFANTIL')
elif y <= 19:
    print('JUNIOR')
elif y <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
