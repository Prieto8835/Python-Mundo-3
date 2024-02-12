print('Tabela paulistão 2024')
print('-~'*30)
times = ('Santos', 'São Paulo', 'São Bernardo', 'Palmeiras', 'Red Bull Bragantino', 'Ponte Preta', 'Novorizontino',
         'Botafogo-SP', 'Agua Santa', 'Mirassol', 'Inter de Limeira', 'Guarani', 'Ituano', 'Portuguesa', 'Corinthians',
         'Santo André')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Posição na qual está o time do Corinthians é: {times.index("Corinthians") + 1}° colocado')
print(f'Times em ordem alfabética {sorted(times)}')
