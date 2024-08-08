#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase:'))
frase01 = frase.split()
print(frase01)
frase02 = ''.join(frase01)
print(frase02)
limite = int((len(frase02)-1)/2)
print(limite)
tamanho = len(frase02)
print(tamanho)

s=0


if len(frase02) % 2 != 0:
    for c in range(0,limite):
        if frase02[c] == frase02[tamanho-1-c]:
            s = s + 1
        else:
            s=s
else:
    s=0

if s == limite:
    print('A frase digitada é um POLINDROMO')
else:
    print('A frase digitada nao é um POLINDROMO')




