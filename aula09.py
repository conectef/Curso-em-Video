from dataclasses import replace


frase = '  Curso em Vídeo Python  ' #uma string é imutável, a não ser que seja atribuida. 
print(frase[::2])
#print('''A poluição gerada e impregnada nas grandes cidades foi em grande parte fruto da urbanização desenfreada ou da atuação de indústrias; porém, deveres não cumpridos pelos homens também proporcionaram toda essa "sujidade".''')
print(frase.upper().count('O'))
#print(len(frase))
print(len(frase.strip()))
# print(frase.replace('Python', 'Abdroid'))
# print(frase)
# print('Curso' in frase) 
# print(frase.lower().find('Vídeo'))
# print(frase.split())
# dividido = frase.split()
# print(dividido[0])
# print(dividido[2][3])  