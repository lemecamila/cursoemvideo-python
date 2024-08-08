# programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite a cidade em que nasceu: ')).strip()

print('A cidade começa com SANTO? {}'.format(cid[:5].upper() == 'SANTO'))