#programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Digite a distancia da sua viagem'))

if dist<=200:
    vlr = 0.5*dist
else:
    vlr = 0.45*dist

# opcao de if e else simplificado: vlr= 0.5*dist if dist<=200 else vlr=dist*0.45

print('O valor da viagem é R${:.2f} reais'.format(vlr))



