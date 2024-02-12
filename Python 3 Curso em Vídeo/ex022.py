name = str(input('Whats your name? ')).strip() #formatado com "str" e colocado ao final "strip()" para cortar os espaços antes e depois de "name"
print(f'Your name in capital letters is: {name.upper()}')
print(f'Your name in lower case is: {name.lower()}')
print(f'Your name has {len(name) - name.count(' ')} letters in total')
divide = (name.split())
print(f'Your first name is {divide[0]} and he has {len(divide[0])} letters')