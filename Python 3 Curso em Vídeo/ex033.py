x = int(input('Write first value: '))
y = int(input('Write second value: '))
z = int(input('Write third value: '))
if (x > y) and (x > z):
    print(f'Greater value is {x}')
if (y > x) and (y > z):
    print(f'Greater value is {y}')
if (z > x) and (z > y):
    print(f'Greater value is {z}')
if (x < y) and (x < z):
    print(f'Lowest value is {x}')
if (y < x) and (y < z):
    print(f'Lowest value is {y}')
if (z < x) and (z < y):
    print(f'Lowest value is {z}')
print('--'*20)
print(f'Maior valor é: {max(x, y, z)}')
print(f'Menor valor é: {min(x, y, z)}')
