#soma dois numeros inteiros, com cores
n1 = int(input('\033[1;34;40mDigite um valor:'))
n2 = int(input('\033[1;31;40mDigite outro valor:\033[m'))
print('A soma entre \033[1;34;40m{}\033[m e \033[1;31;40m{}\033[m é \033[1;33;40m{}\033[m'.format(n1,n2,n1+n2))

