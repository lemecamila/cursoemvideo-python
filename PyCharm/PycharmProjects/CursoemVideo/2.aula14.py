'''Modelo For'''
for c in range (1,10):
    print(c)
print('Fim For')

'''Modelo While'''
a = 1
while a<10:
    print(a)
    a = a + 1
print('Fim While')

'''Se souber os limites do range podemos usar for ou while'''
'''Se nao soubermos o limite do range, usar o while. Ex:'''
n=1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero inteiro:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else: impar += 1

print('Voce digitou {} numeros pares e {} numeros impares.'.format(par,impar))
print('Fim')
