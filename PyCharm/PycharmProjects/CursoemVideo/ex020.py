#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a = str(input('Primeiro Aluno: '))
b = str(input('Segundo Aluno: '))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto Aluno: '))
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem de apresentacao será:{}'.format(lista))
