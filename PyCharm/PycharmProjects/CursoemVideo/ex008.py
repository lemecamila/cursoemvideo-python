m = float(input('Digite uma medida em metros: '))

print('A medida de {} metros, corresponde a: '
      '\n {}km \n {}hm \n {}dam \n {}m \n {}dm \n {}cm \n {}mm'
      .format(m,m/1000,m/100,m/10,m,m*10,m*100,m*1000))
