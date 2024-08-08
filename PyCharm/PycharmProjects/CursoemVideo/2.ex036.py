# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa que deseja comprar:'))
salario = float(input('Digite o valor do seu salario:'))
anos = int(input('Digite em quantos anos voce gostaria de quitar a casa'))

if casa/(anos*12) < salario*0.3:
    valor = casa/(anos*12)
    print('O valor da prestacao será de R${}'.format(valor))
elif casa/(anos*12) >= salario*0.3:
    anos = (casa/(salario*0.3))/12
    valor = casa / (anos * 12)
    print('Voce terá que quitar a casa em {} anos com uma prestacao de R${}. Ou nao poderá compra-la'.format(anos,valor))
