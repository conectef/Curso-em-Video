medida = float(input('Uma medida em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
dec = medida / 10
nan = medida * 1e+9
hec = medida / 100

print('A medida de {}m corresponde a {:.0f}cm, {:.0f}km , {:.0f}dec , {:.0f}nan , {:.0f}hec e {:.0f}mm'.format(medida, cm, mm, km, dec, nan, hec))
