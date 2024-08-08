# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# print(f'Resultados: \n'
#       f'a) O total gasto na compra foi de R${soma} \n'
#       f'b) {cont} produtos custam mais do que R$1000,00 reais \n'
#       f'c) O produto mais barato é: {nome}')
#
# nome = str(input('Digite o nome do produto: '))
# menor = float(input('Digite o preco do produto: '))
# resp = str(input('Deseja continuar? [S/N] \n')).strip().upper()
# soma = menor
# if menor > 1000:
#     cont = 1
# else:
#     cont = 0
#
# while resp == 'S':
#
#     prod = str(input('Digite o nome do produto: '))
#     preco = float(input('Digite o preco do produto: '))
#
#     soma = soma + preco
#
#     if preco > 1000:
#         cont += 1
#
#     if preco < menor:
#         nome = prod
#         menor = preco
#
#     resp = str(input('Deseja continuar? [S/N] \n')).strip().upper()
#
#     while resp != 'S' and resp != 'N':
#         resp = str(input('Deseja continuar? [S/N] \n')).strip().upper()
#
#
#     if resp == 'N':
#         break
#
# print(f'Resultados: \n'
#       f'a) O total gasto na compra foi de R${soma} \n'
#       f'b) {cont} produtos custam mais do que R$1000,00 reais \n'
#       f'c) O produto mais barato é: {nome}')
#

cont = soma = totmil = menor = 0
while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    cont += 1
    soma += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] \n')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Resultados: \n'
      f'a) O total gasto na compra foi de R${soma} \n'
      f'b) {totmil} produtos custam mais do que R$1000,00 reais \n'
      f'c) O produto mais barato é: {nome}')