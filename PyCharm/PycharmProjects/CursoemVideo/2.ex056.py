idade_soma = 0
idade_maior = 0
count = 0
for c in range (0,4):
    nome = str(input('Digite o nome da pessoa {}: '.format(c+1)))
    idade = int(input('Digite a idade da pessoa {}: '.format(c+1)))
    sexo = str(input('Digite o sexo da pessoa {}, sendo: \n'
                     ' 1)FEMININO \n'
                     ' 2)MASCULINO \n'.format(c+1)))

    '''if sexo != 1 and sexo != 2:
        sexo =str(input('Nao existe essa opcao para sexo, digite o sexo da pessoa {}, sendo: \n'
                        '1)FEMININO \n'
                        '2)MASCULINO \n'.format(c+1))) TERIA QUE USAR WHILE'''


    idade_soma = idade_soma + idade

    if idade > idade_maior and sexo == 2:
        idade_maior = idade
        nome_maior = nome

    if idade < 20 and sexo == 1:
        count = count + 1

print('A somatória das idades informadas é {} e a média é {}'.format(idade_soma,idade_soma/4))

if idade_maior == 0:
    print('Nao existe homem na lista de nomes')
else:
    print('O nome do homem mais velho é: {}, ele possui {} anos'.format(nome_maior,idade_maior))

if count == 0:
    print('Nao existe mulheres com menos de 20 anos')
else:
    print('Existem {} mulheres com menos de 20 anos'.format(count))





