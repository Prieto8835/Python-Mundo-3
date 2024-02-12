name = str(input('Whats your name? ')).strip()
if name == 'Alejandro':
    print('Most beautiful name!')
elif name == 'Juanito':
    print('Nice name!')
else:
    print('More generic name!')
print(f'Good morning, {name}!')

n1 = float(input('Write first note: '))
n2 = float(input('Write second note: '))
m = (n1+n2)/2
if m >= 6.0:
    print('Congratulations!')
else:
    print('Dumb!')
    