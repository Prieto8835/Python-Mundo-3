from random import randint
from time import sleep
x = 'Pedra', 'Papel', 'Tesoura'
y = int(input('[0] Pedra' '\n[1] Papel' '\n[2] Tesoura' '\nSua Opção: '))
print('--'*20)
print('Pedra...')
sleep(0.65)
print('Papel...')
sleep(0.65)
print('Tesoura...')
sleep(0.65)
print('--'*20)
s = randint(0, 2)
print(f'Escolha da máquina: {x[s]}')
print(f'Escolha do jogador {x[y]}')
if s == y:
    print('Houve um EMPATE')
elif s == 0 and y == 1:
    print('Jogador GANHOU!')
elif s == 0 and y == 2:
    print('Máquina GANHOU!')
elif s == 1 and y == 0:
    print('Jogador GANHOU!')
elif s == 1 and y == 2:
    print('Jogador GANHOU!')
elif s == 2 and y == 0:
    print('Jogador GANHOU!')
elif s == 2 and y == 1:
    print('Máquina GANHOU!')
elif y > 2:
    print('OPÇÃO INCORRETA!')
print('--'*20)
