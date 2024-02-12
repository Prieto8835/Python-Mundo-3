palavras = ('Programacao', 'Python', 'Programador', 'Fighting Games', 'Euro Truck Simulator', 'Street Fighter',
            'Porradaria', 'Pancada', 'Hadouken', 'Ken', 'Chatuba de Mesquita')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
