frase = 'Curso em Vídeo Python!'
print(frase[0:12:2]) #[inicio:final:quantas casas pular]
print(frase.count('o')) #conta quantas vezes tem letra 'o'
print(frase.upper().count('o')) #conta quantas vezes tem letra 'o' em MAISCULO
print(frase.upper()) #letra maiscula
print(frase.lower()) #letra minicusla
print(len(frase)) #conta quantos caracteres tem no string
print(len(frase.strip())) #conta quantos caracteres tem no string e reitira espaços vazios
print((frase.replace('Python', 'Android')))
frase = (frase.replace('Python', 'PHP'))
print(frase)
print('Curso'in frase) #retorna com verdadeiro ou falso
print('curso'in frase) #retorna com verdadeiro ou falso
print(frase.lower().find('vídeo')) #verifica se tem 'vídeo' dentro da variável frase, em letras minúsculas por conta do "lower"
print(frase.find('VÍDEO')) #caso retorne -1 significa inexistente
dividido = (frase.split()) #divide a frase
print(dividido)
print(dividido[2]) #mostra o primeiro item da lista dividido
print(dividido[2][3]) #mostra o segundo item da lista e mostra terceiro caractere do item
print("""Python é uma linguagem de programação de alto nível, interpretada de script, 
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991. """)
