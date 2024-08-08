#ler tres numeros e mostrar qual o maior e qual o menor
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1>num2 & num2>num3:
    print('O primeiro numero é o maior e o terceiro numero é o menor')
else:
    if num2>num1 & num1>num3:
        print('O segundo numero é o maior e o terceiro numero é o menor')
    else:
        if num1>num3 & num3>num2:
            print('O primeiro numero é o maior e o segundo numero é o menor')
        else:
            if num2>num3 & num3>num1:
                print('O segundo numero é o maior e o primeiro numero é o menor')
            else:
                if num3>num2 & num2>num1:
                    print('O terceiro numero é o maior e o primeiro numero é o menor')
                else:
                    if num3>num1 & num1>num2:
                        print('O terceiro numero é o maior e o segundo é o menor')



# opcao otimizada:
# menor = num1
# maior = num1
# if num2<num1 and num2<num3
    #menor = num2
# if num3<num1 and num3<num2
    #menor = num3
# if num2>num1 and num2>num3
    #maior = num2
# if num3>num1 and num3>num2
    #maior = num3

#print('o maior numeor é {}'.format(maior))
#print('o menor numero é {}'.format(menor))

