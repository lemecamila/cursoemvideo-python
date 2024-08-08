s = 0
for c in range(0,6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        s = s + num
    else:
        s = s
print('A somatoria dos números pares digitados é: {}'.format(s))