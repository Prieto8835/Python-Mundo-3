from datetime import date
x = int(input('Write a year(enter 0 for the current year): '))
if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0: #símbolo != é diferente
    print(f'{x} is leap year') #ano bissexto
else:
    print(f'{x} is not leap year')
