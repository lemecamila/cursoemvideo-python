#programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

''' – Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

import datetime
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = datetime.date.today()
idade = atual.year - ano
print('Idade do atleta: {} anos'.format(idade))

if idade <= 9:
    print('Categoria Mirim')
elif idade<=14:
    print('Categoria Infantil')
elif idade<=19:
    print('Categoria Junior')
elif idade <=25:
    print('Categoria Senior')
else:
    print('Categoria Master')
