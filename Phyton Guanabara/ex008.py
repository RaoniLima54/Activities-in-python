m = float(input('Digite o valo em metros : '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm= m*1000

print('A tebela de medidas foi gerada : \nEm quilômetros {} km \nEm hectômetro é {} hm \nEm decametro é {} dam \nEm metros {:.0f} m \nEm decimetro é {:.0f} dm \nEm centímetros é {:.0f} cm \nEm milímetros é {:.0f} mm'.format(km,hm,dam,m,dm,cm,mm))

