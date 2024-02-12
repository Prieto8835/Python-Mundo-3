s = str(input('Selecione seu sexo: [M/F] ')).upper().strip()
while s != 'F' and s != 'M':
    s = str(input('Opção incorreta! Por favor selecione uma opção válida: [M/F] ')).upper().strip()
print(f'Opção {s} registrada com sucesso! ')
