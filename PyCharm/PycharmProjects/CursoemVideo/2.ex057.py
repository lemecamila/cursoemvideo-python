'''Faca um programa que leia o sexo de uma pessoa que só aceite os valores 'F' ou M' '''
'''Se digitar errado, peca o valor novamente ate digitar certo'''
sexo = 'J'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa [F/M]: \n Feminino (F) \n Masculino (M) \n')).upper().strip()[0]

print('Sexo registrado com sucesso: {}'.format(sexo))
