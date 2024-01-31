casa = float(input('Qual o valor da casa? '))
Sal = float(input('Qual o valor do seu salário? '))
T = int(input('Em quantos anos vai pagar? '))
P = casa / (T * 12) 
if (Sal * 0.3) >= P :
    print('Empréstimo aprovado! ')
else:
    print('Empréstimo negado! ')

# import math

# print("Calculadora Financiamento")
# salario = float(input("Informe o salário: "))
# casa = float(input("Informe o valor da casa: "))
# meses = float(input("Informe a quatidade de meses: "))

# res = (casa/meses)/salario

# if res < 0.3:
#     print("Seu financiamento foi aprovado!")
# else:
#     print("Seu finaciamento foi negado, desculpe.")   