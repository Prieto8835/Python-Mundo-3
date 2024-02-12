from pprint import pprint
x = str(input('Escreva qualquer coisa: ')).strip().upper()
print(x.count('A')) #quantas vezes aparece
print(x.find('A')+1) #qual posição aparece primeira vez
print(x.rfind('A'))
#print(len(x)-1 - x[::-1].find('A')) #saber posição exata do último caractere "A" na string (Tamanho - Tamanho pelo valor)
pprint(list(enumerate(x))) #mostra posição exata de cada caractere na string