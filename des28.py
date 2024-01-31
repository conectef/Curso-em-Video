import random
num = int(input('Escolha um número de 0 até 5: '))
lista = [0, 1, 2, 3, 4, 5]
r = random.choice(lista) 
print('O numero que eu pensei foi {}'.format(r))
if num == r:
    print('Você acertou!')
else: 
    print('Você errou! ')
