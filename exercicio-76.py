listagem = ('Teclado', '85.00',
            'Mouse', '55.00',
            'Notebook SamSom', '2550.00',
            'Arroz', '12.00',
            'Feijão', '08.50',
            'Fone', '35.00',
            'Açucar', '09.50',
            'Café', '05.50',
            'Mesa', '800.00')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'\n{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6}')


