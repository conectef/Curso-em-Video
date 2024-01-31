from cv2 import split


n = str(input('Qual o seu nome completo: ')).strip() 
nome = n.split()
print('Muito prazer em te conhecer! ')
print('O primeiro nome é {}'.format(nome[0]))
print('O ultimo nome é {}'.format(nome[len(nome)-1]))
