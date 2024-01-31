n = input('Digite algo: ')          #todo objeto tem atributos e métodos
print(' O tipo primitivo desse valor é ', type(n))
print('Só tem espaço? ', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúculas?', n.islower())
print('Está capitalizada?', n.istitle())