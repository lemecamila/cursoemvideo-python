#ler algo e informar seu tipo primitivo e todas as informacoes

algo = input('Digite algo: ') #funcao input sempre retorna str
print('O tipo primitivo é:',type(algo))
print('Só tem espacos? ', algo.isspace())
print('É numérico? ', algo.isnumeric())
print('É alfabético?',algo.isalpha())
print('É alfanumúmerico?', algo.isalnum())
print('Está em maiúsculas?',algo.isupper())
print('Está em minúsculas?',algo.islower())
print('Está capitalizada?', algo.istitle())



