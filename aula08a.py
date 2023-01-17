
# import emoji

### Des 16 ###
# import math
# num = float(input('Digite um número: '))
# int = math.floor(num)    #inteiro
# print('O número {:.3f} tem a parte inteira {}'.format(num, int))

### Des 17 ###
#import math
# from math import floor, hypot
# num = float(input('Digite o cateto 1: '))
# num2 = float(input('Digite o cateto 2: '))
# print('A hipotenusa desse triangulo é {:.2f}'.format(hypot(num, num2))) 

### Des 18 ###

# from math import radians, sin, cos, tan
# num = float(input('Digite o ângulo: '))
# seno = sin(radians(num))
# cosseno = cos(radians(num))
# tangente = tan(radians(num))
# print('O ângulo de {}, tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(num, seno, cosseno, tangente)) 

# import math
# num = float(input('Digite o ângulo: '))
# seno = math.sin(math.radians(num))
# cosseno = math.cos(math.radians(num))
# tangente = math.tan(math.radians(num))
# print('O ângulo de {}, tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(num, seno, cosseno, tangente)) 


### Des 19 ###
# import random
# aluno1 = str(input('Primeiro aluno: '))
# aluno2 = str(input('Segundo aluno: '))
# aluno3 = str(input('Terceiro aluno: '))
# aluno4 = str(input('Quarto aluno: '))
# lista = [aluno1, aluno2, aluno3, aluno4]
# num = random.choice(lista)

# print(aluno1, aluno2, aluno3, aluno4)

# print('O aluno escolhido foi {}'.format(num)) 

### Des 20 ###
import random
from random import shuffle
aluno1 = str(input('\033[31mPrimeiro aluno: \033[m'))
aluno2 = str(input('\033[32mSegundo aluno: \033[m'))
aluno3 = str(input('\033[33mTerceiro aluno: \033[m'))
aluno4 = str(input('\033[34mQuarto aluno: \033[m'))
lista = [aluno1, aluno2, aluno3, aluno4]
num = shuffle(lista) # pode acontecer de cair na mesma ordem que você digitou, isso é aleatório. 

print(aluno1, aluno2, aluno3, aluno4)

print('A ordem de apresentação foi essa ')
print(lista)

### Des 21 ###
# import playsound
# from playsound import playsound
# num = ('https://www.youtube.com/watch?v=_Yhyp-_hX2s&ab_channel=msvogue23')
# print('num')

import pygame
pygame.init()
pygame.mixer.music.load('d02.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


# num = int(input('Digite o número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, raiz))
# print(emoji.emojize('Olá, mundo :earth_americas:', use_aliases=True))





