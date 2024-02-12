cont = 0
while True:
    tab = int(input('Write a number for multiplication table: '))
    if tab < 0:
        print('Its over, thank you for playing! ')
        break
    for c in range(0, 11):
        result = tab * cont
        print(f'{tab} x {c:2} = {result}')
        cont += 1
        if cont > 10:
            cont = 0


while True:
    tab = int(input('Write a number for multiplication table: '))
    if tab < 0:
        print('Its over, thank you for playing! ')
        break
    for c in range(0, 11):
        print(f'{tab} x {c:2} = {tab*c}')
