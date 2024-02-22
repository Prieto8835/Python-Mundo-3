grupo1 = list()
grupo1.append('Alejandro')
grupo1.append(21)
grupo2 = list()
grupo2.append(grupo1[:])
grupo1[0] = 'Juanito'
grupo1[1] = 65
grupo2.append(grupo1[:])
print(grupo2)

galera = [['Alejandro', 21], ['Luzia', 58], ['Juanito', 65]]
print(galera)
print(galera[0][1])
print(galera[1][0])
print(galera[2][1])

for pessoa in galera:
    print(f'A pessoa {pessoa[0]} tem {pessoa[1]} anos de idade! ')

totmaior = totmenor = 0
grupo = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    grupo.append(dado[:])
    dado.clear()
print(grupo)

for pessoa in grupo:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade! ')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade! ')
        totmenor += 1
print(f'Ao total temos {totmaior} maiores de idade e {totmenor} menores de idade! ')
