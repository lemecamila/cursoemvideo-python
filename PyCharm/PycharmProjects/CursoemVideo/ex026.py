#programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
txt = str(input('Digite uma frase: ')).strip()
txt1 = txt.upper()
print('A letra a aparece {} vezes na frase acima'. format(txt1.count('A')))
print('A primeria posicao que a letra A apareceu é: {}'.format(txt1.find('A')+1))
print('A ultima posicao que a letra A apareceu é: {}'.format(txt1.rfind('A')+1))