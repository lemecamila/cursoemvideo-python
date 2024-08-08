'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso/(altura * altura)
print('Seu IMC é {:.2f}'.format(IMC))

if IMC <18.5:
    print('Voce está abaixo do peso')
elif IMC >=18.5 and IMC<25:
    print('Voce esta no peso ideal')
elif IMC=>25 and IMC<30:
    print('Voce esta com sobrepeso')
elif IMC=>30 and IMC<40:
    print('Voce esta com obesidade')
else:
    print('Voce esta com obesidade morbida')
