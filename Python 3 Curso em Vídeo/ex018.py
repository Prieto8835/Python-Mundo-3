import math
ang = float(input('Ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'Seno: {sen:.2f} \nCosseno: {cos:.2f}  \nTangente {tan:.2f}')

#from math import radians, sin, cos, tan
#sen = sin(radians(ang))
#cos = cos(radians(ang))
#tan = tan(radians(ang))
#print(sen, cos, tan)