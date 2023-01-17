nome = str(input('Qual é o seu nome: '))
if nome == 'Gustavo':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
# if m>=6.0:
#     print('Sua média foi boa! PARABÉNS!')
# else:
#     print('Sua média foi ruim! ESTUDE MAIS!')
print('\033[30;44mPARABÉNS\033[m' if m>=6 else '\033[1;31;43mESTUDE MAIS!\033[m') #condição simplificada  
