co = float(input('Write a height: '))
ca = float(input('Write a width: '))
h = co**2 + ca**2
h = h**(1/2)
print(f'Result hypotenuse is {h:.2f}')
print(f'With co {co**2} and ca {ca**2} hypotenuse is {(co**2+ca**2)**(1/2):.2f}')

from math import hypot
hi = hypot(co,ca)
print(f'{hi:.3}')