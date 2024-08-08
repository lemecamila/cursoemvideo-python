#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano = int(input('Digite seu ano de nascimento: '))

atual = datetime.date.today()
print(atual)

idade = atual.year - ano

if idade == 18:
    print('Voce está na idade certa para se alistar')
elif idade<18:
    print('Voce ainda nao esta na idade de alistamento. Faltam {} anos para voce se alistar. Seu alistamento sera em {}'.format(18-idade,atual.year+18-idade))
else:
    print('Voce já passou {} anos da idade de alistamento. O seu ano de alistamento foi {}'.format(idade-18, atual.year-idade+18))


