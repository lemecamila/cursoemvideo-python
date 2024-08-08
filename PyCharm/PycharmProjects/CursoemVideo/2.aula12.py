nome = str(input('Qual o seu nome?'))
if nome.upper()=='CAMILA':
    print('Que nome bonito')
elif nome.upper()=='ANA' or nome.upper() == 'PEDRO':
    print('Seu nome é muito comum no Brasil')
elif nome.upper() in 'JOANA FABIANA SARA AMANDA':
    print('Seu nome é feminino')
#else:
    #print('Seu nome é bem comum')

print('Tenha um bom dia {}'.format(nome))