x = int(input('Write a number for multiplication table: '))
print('=='*7)
for c in range(0, 11):
    print(f'{x} x {c:2} = {x * c}')
print('=='*7)
