lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
a = (2, 4, 6)
b = (3, 5, 7)
c = a + b
print(c)
print(c[1]) #mostra o elemneto na posição 1
print(c[1:]) #mostra valores a partir da posição 1
print(c[-2]) #mostra o penúltimo valor
print(len(c)) #mostra quantidade de números dentro da soma das tuplas
print(c.count(5)) #quantas vezes aparece número 5 em C
print(c.index(5)) #mostra a posição do número
pessoa = ('Alejandro', 21, 'M', 65.52)
del(pessoa)
print(pessoa)
