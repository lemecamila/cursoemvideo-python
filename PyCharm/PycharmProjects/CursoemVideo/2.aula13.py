for c in range (1,4):
    print('oi')
print('FIM')

for c in range (0,4):
    print('hi')
print('END')

for c in range (4,0,-1):
    print('hi')
print('End')

n=int(input('Digite um numero: '))
for c in range (0,n+1):
    print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i,f+1,p):
    print(c)

s=0
for c in range  (0,4):
    num = int(input('Digite um numero: '))
    s = s + num # s+= num

print('A somatoria de todos os numeros é: {} '.format(s))

