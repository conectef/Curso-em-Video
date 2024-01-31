num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# verificando quem é menor
menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
# verificando quem é maior
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3> num2:
    maior = num3
print('O menor número É {}'.format(menor))
print('O maior número É {}'.format(maior))





