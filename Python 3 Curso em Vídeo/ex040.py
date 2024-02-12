n1 = float(input('First note: '))
n2 = float(input('Second note: '))
m = (n1+n2)/2
if m < 5.0:
    print(f'Com as notas de {n1} e {n2}, obtendo a média de {m} o aluno está REPROVADO!')
elif 4.9 < m < 7.0:
    print(f'Com as notas de {n1} e {n2}, obtendo a média de {m} o aluno está em RECUPERAÇÃO!')
else:
    print(f'Com as notas de {n1} e {n2}, obetendo a média de {m} o aluno está APROVADO!')
