#programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite um ano para verificar se é Bissexto ou digite 0 para analisar o ano atual'))
if ano == 0:
    ano = date.today().year


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')

else:
    print('O ano nao é bissexto')

