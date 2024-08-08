# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = flag = cont = 0

while flag != 999:
    flag = int(input('Digite um numero inteiro. (Para encerrar digite 999): '))

    if flag != 999:
        cont = cont + 1
        soma = soma + flag

print('voce digitou {} numeros e a somatoria deles foi {}'.format(cont,soma))