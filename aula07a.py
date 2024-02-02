
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





p = float(input('Digite o preço:'))
p1 = p*0.05
print('Preço original:', p, 'e seu novo preço com 5% de desconto será:', p1)


# Ordem de precedencia
# 1 ()
# 2 **
# 3 * // %
# 4 + -