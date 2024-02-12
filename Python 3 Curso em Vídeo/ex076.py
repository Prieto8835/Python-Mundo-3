produtos = ('Computador', 3000, 'Xbox Series S', 1600,  'Playstation 2', 450, 'Playstation 3', 600,
            'PSP', 300, 'Super Nintendo', 500, 'Mega Drive', 350, 'Tv 43', 1400, 'Som Edifier', 400, 'Controle Arcade',
            200, 'Cadeira Gamer', 620)
print('-'*40)
print(f'{"PRODUTOS":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
