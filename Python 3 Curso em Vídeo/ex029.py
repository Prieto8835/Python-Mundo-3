x = int(input('Write the speed of the car KM/H: '))
if x > 80:
    print('You have been fined! Be more careful!')
    y = (x - 80)*7
    print(f'Fine value is U${y:.2f}')
else:
    print('You were not fined. Keep driving carefully, have a nice day')
