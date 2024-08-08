#conversao de bases estudar
# leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um numero inteiro:'))
print('Escolha qual a base de conversao. Sendo: \n'
      '(1) BINARIO\n'
      '(2) OCTAL\n'
      '(3) HEXADECIMAL\n')
opcao = int(input('Sua escolha:'))

if opcao == 1:
    print('{} convertido para BINARIO é {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opcao inexistente')