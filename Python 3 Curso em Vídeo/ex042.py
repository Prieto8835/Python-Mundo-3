a = float(input('Write first value: '))
b = float(input('Write second value: '))
c = float(input('Write third value: '))
c1 = a < (b+c)
c2 = b < (a+c)
c3 = c < (a+b)
if c1 and c2 and c3 == True:
    print('Pode-se formar um triângulo!')
    if a == b == c:
        print('Triângulo equilátero (TODOS OS LADOS IGUAIS)')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles (DOIS LADOS IGUAIS)')
    else:
        print('Triângulo escaleno (TODOS OS LADOS DIFERENTES)')
else:
    print('Com esses valores não pode-se formar um triângulo!')
