#programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))

print('A Progressao Aritimetica que inicia com o termo {} e possui razao {} é:'.format(termo,razao))

'''for c in range(termo,termo*10+1,razao):
    print(c)'''


'''Opcao While'''
cont = 1
tam = 10
total = 0
while tam != 0:
    total = total + tam
    while cont <= total:
        print('{}, '.format(termo), end='')
        termo = termo + razao
        cont += 1

    opcao = str(input('Voce gostaria de visualizar mais alguns termos dessa PA? [S/N]')).upper()
    if opcao == 'S':
        tam = int(input('Quantos termos a mais voce gostaria de visualizar?'))
    else:
        tam = 0

print('Progressao finalizada com {} termos mostrados'.format(total))

print('Fim do Programa')
