vlr = float(input('Digite o preco normal do produto:'))
cond = int(input('Digite o numeor correspondente a condicao de pagamento desejada. Sendo: \n '
                 '(1) A vista no Dinheiro \n '
                 '(2) A vista no cartao \n '
                 '(3) Até duas vezes no cartao \n'
                 ' (4) Tres vezes ou mais no cartao \n'))
if cond == 1:
    print('O preco do produto é: R${:.2f}'.format(vlr*0.9))
elif cond == 2:
    print ('O preco do produto é: R${:.2f}'.format(vlr*0.95))
elif cond == 3:
    print('O preco do produto é R${:.2f}. Voce pagará em duas parcelas de R${:.2f}'. format(vlr,vlr/2))
elif cond == 4:
    parcela = int(input('Quantas parcelas? '))
    print('O preco do produto é R${:.2f}. Voce pagará {} parcelas de R${:.2f} cada'.format(vlr*1.2,parcela,vlr*1.2/parcela))
else:
    print('Opcao invalida!')



