
# while True: caracteriza looping infinito

# cont = 0
# while True:
#     print(cont,'->', end='')
#     cont +=1
# print('Ácabou')

#
n = 0
s = 0
nome ='camila'
# while n != 999:
#     s = s + n
#     n = int(input('Digite um numero: '))
#
# print('A soma vale {}'.format(s))

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s:.2f}')
print(f'Seu nome é: {nome:-20} ok')

