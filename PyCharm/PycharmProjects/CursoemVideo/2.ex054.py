#programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
atual = datetime.date.today().year
s=0
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento'))
    if atual - ano >= 18:
        s = s + 1
    else:
        s=s
print('{} pessoas já atingiram a maior idade. {} ainda nao'.format(s,7-s))



    


