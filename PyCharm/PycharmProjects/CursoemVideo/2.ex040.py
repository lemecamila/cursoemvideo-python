#programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Sua media foi: {:.1f}'.format(media))

if media <5:
    print('\033[7;31mREPROVADO\033[m')

elif 6.9>=media>=5 :
    print('\033[7;33mRECUPERACAO\033[m')

else:
    print('\033[7;34mAPROVADO\033[m')
