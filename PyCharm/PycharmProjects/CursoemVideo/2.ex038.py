#Exercício Python 038:
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro numero inteiro:'))
num2  = int(input('Digite o segundo numero inteiro:'))

if num1 == num2:
    print('Os numero sao iguais')
elif num2 > num1:
    print('O segundo numero é maior que o primeiro numero')
else:
    print('O primeiro numero é maior que o segundo numero')

