k = float(input('Qual é a distância da sua viagem em km? '))
l = 200
p = k*0.45
p2 = k*0.5
if k<=l:
    print('A distância de {}km, a passagem será {:.2f}reais'.format(k, p2))
else:
    print('A viagem de {}km, custará {:.2f}reais'.format(k, p))