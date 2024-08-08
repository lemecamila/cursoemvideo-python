#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um numero de 0 a 9999'))


'''n = str(num)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

print('Unidade: {}'.format(num//1%10))
print('Dezena: {}'.format(num//10%10))
print('Centena: {}'.format(num//100%10))
print('Milhar: {}'.format(num//1000%10))