n = int(input('Digite o numero de termos da sequencia de Fibonatti que deseja ver:'))
c=0
t1=0
t2 = 1

print('{} , {} '.format(t1,t2),end='')

while c<(n-2):
    t3 = t1 + t2
    print(', {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    c += 1
print('\n FIM')


