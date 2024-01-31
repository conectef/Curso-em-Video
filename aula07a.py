n1 = int(input('Nota1: '))
n2 = int(input('Nota2: '))
metros = float(input('Quantidade em metro: '))
n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
tabuada = int(input('Insira um número: '))
for count in range(10):
    print('%d x %d = %d' % (tabuada, count+1, tabuada*(count+1)) )

din = float(input('Dinheiro na carteira: '))
saldo = din / 3.27
print('Saldo em dolar é {:.2f}'.format(saldo))
l = int(input('Largura: '))
a = int(input('Altura: '))
area = l * a / 2
print('Qtd necessária de tinta é {}l'.format(area))

preco = float(input('Preço sem desconto: '))
desc =  preco - (preco * 0.05)
print('Preço com desconto de 5% {} reais'.format(desc))

s = float(input('Valor do salário sem aumento: '))  # des 13
au = s + (s * 0.15)
print('Salário com aumento de 15% é de {:.2f} reais'.format(au))

cent = metros * 100
mili = metros * 1000
s1 = n1+n2
s = (n1+n2)/2
m = n1*2
d = n1/n2
di = n1//n2
e = n1**n2

n = int(input('Digite um número: '))    #des 05
f = n+1
g= n-1
print('Analisando o número {}, Seu sucessor é {} e seu antecessor é {}'.format(n, f, g))
print('Analisando o número {}, Seu sucessor é {} e seu antecessor é {}'.format(n, (n+1), (n-1))) #mais variáveis usa mais memória

n1 = int(input('Digite um número: '))
h = n1*2
i = n1*3
j = n1**2
l = n1**(1/2)
print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

print('Seu dobro é {}, seu triplo é {} \ne sua raiz quadrada é {:.2f}'.format(h, i, l))
print('Seu dobro é {}, seu triplo é {} \ne sua raiz quadrada é {:.2f}'.format((n1*2), (n1*3), (n1**(1/2))))
print('Seu dobro é {}, seu triplo é {} \ne sua raiz quadrada é {:.2f}'.format((n1*2), (n1*3), pow(n1,(1/2))))
print('A soma das suas notas é essa {}, e sua média é essa {}'.format(s1, s))
print('Metros em cm é {}, e metros em ml é {}'.format(cent, mili))

p = float(input('Digite o preço:'))
p1 = p*0.05
print('Preço original:', p, 'e seu novo preço com 5% de desconto será:', p1)


# Ordem de precedencia
# 1 ()
# 2 **
# 3 * // %
# 4 + -