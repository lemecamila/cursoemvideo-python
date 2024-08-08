# pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
km = float(input('Digite o número de km rodados pelo carro alugado:' ))
dias = int(input('Digite o número de dias que o carro ficou alugado:'))
print('O valor a pagar pelo carro que rodou {}km e ficou alugado por {} dias é R${:.2f}'
      .format(km,dias,60*dias+0.15*km))