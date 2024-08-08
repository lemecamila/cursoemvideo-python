#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

'''– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

s=0
for c in range(1,500,2):

    if c % 3 == 0:
        s = s + c
    else:
        s = s
print('A soma dos números impares e múltiplos de 3, no intervalo de 1 a 500 é: {}'.format(s))
#20667