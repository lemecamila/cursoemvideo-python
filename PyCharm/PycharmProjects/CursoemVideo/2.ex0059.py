'''Crie um programa qye leia 2 valores e mostre o menu:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa'''

opcao = 0
num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))

while opcao !=5:
    opcao = int(input('Digite a opcao abaixo desejada: \n '
      '(1) Somar \n '
      '(2) Multiplicar \n '
      '(3) Maior \n '
      '(4) Novos Numeros \n'
      '(5) Sair \n'))
    if opcao == 1:
        soma = num1 + num2
        print('A soma é: {}'.format(soma))

    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicacao é: {}'.format(mult))

    elif opcao == 3:
        if num1 > num2:
            print('O primeiro numero: {} é maior que o segundo: {}'.format(num1,num2))
        elif num2 > num1:
            print('O segundo numero: {} é maior que o primeiro: {}'.format(num2,num1))
        else:
            print('Os numeros sao iguais')

    elif opcao == 4:
        num1 = int(input('Digite o primeiro numero inteiro: '))
        num2 = int(input('Digite o segundo numero inteiro: '))

    elif opcao !=1 and opcao !=2 and opcao !=3 and opcao !=4 and opcao !=5:
        print('Opcao Incorreta')


print('Voce saiu do programa')
