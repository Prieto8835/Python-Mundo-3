x = input('Write a value: ')
divide = (x.split())
a = (divide[0][3])
b = (divide[0][2])
c = (divide[0][1])
d = (divide[0][0])
print(f'Unidades: {a} \nDezenas: {b} \nCentenas: {c} \nMilhares: {d}')

y = int(input('Write a value: '))
u = y//1 % 10
d = y//10 % 10
c = y//100 % 10
m = y//1000 % 10
print(f'Unidades: {u} \nDezenas: {d} \nCentenas: {c} \nMilhares: {m}')