# ergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o salario: '))
if salario > 1250:
    print('Novo Salario é {}'.format(1.1*salario))
else:
    print('Novo Salario é {}'.format(1.15*salario))
    

