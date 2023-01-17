sal = float(input('Qual é o seu salário? R$ '))
if sal > 1250:
    novo = sal + (sal * 0.1)
else:
    novo = sal + (sal * 0.15)
print('O seu salário antigo era de R$ {:.2f} e agora é R$ {:.2f}'.format(sal, novo))
