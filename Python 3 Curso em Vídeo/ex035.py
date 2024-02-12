a = float(input('Write first value: '))
b = float(input('Write second value: '))
c = float(input('Write third value: '))
c1 = a < (b+c)
c2 = b < (a+c)
c3 = c < (a+b)
print(c1, c2, c3)
if c1 and c2 and c3 == True:
    print('Pode-se formar um triângulo!')
else:
    print('Com esses valores não pode-se formar um triângulo!')
