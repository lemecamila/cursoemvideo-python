'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip()
print('O nome maiúsculo é: {}'.format(nome.upper()))
print('O nome minusculo é: {}'.format(nome.lower()))

print('O numero de caracter do nome é: {}'.format(len(nome) - nome.count(' ')))

#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('O primeiro nome é {} e possui {} letras'.format(separa[0],len(separa[0])))
