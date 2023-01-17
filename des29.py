v = int(input('Qual sua velocidade? '))
lim = 80
m = (v-lim)*7
if v>lim:
    print('Sua multa é R${:.2f} por está na velocidade {}km/h, em uma pista de {}km/h'.format(m, v, lim))
else: 
    print('Parabéns você está no limite da via! ')

    
