#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# f'a) Existem {cont_idade} pessoas com mais de 18 anos\n'
# f'b) Existem {cont_sexo} homens cadastrados\n'
# f'c) Existem {cont} mulheres menores de 20 anos')

cont_sexo = cont_idade = cont = 0
while True:
    print('CADASTRE UMA PESSOA\n')
    idade = int(input('Idade: '))
    sexo = ' '
    resp = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] \n')).strip().upper()[0]

    if sexo == 'M':
        cont_sexo += 1
    if idade > 18:
        cont_idade += 1
    if sexo == 'F' and idade < 20:
        cont += 1

    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] \n')).strip().upper()

    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] \n')).strip().upper()

    if resp == 'N':
        break

print(f'RESULTADO DO CADASTRO:\n'
      f'a) Existem {cont_idade} pessoas com mais de 18 anos\n'
      f'b) Existem {cont_sexo} homens cadastrados\n'
      f'c) Existem {cont} mulheres menores de 20 anos')


