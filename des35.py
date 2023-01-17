a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    print('Eles podem formar um triangulo ')
else:
    print('Eles não podem formar um triangulo ')
    

