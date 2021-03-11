total = totmil = menor = cont = 0
barato = ' '
while True:
    n = str(input('nome do produto'))
    p = float(input('preco do produto'))
    cont += 1
    total += p
    if p > 1000:
        totmil += 1
    if cont == 1 or p < menor:
        menor = p
        barato = n
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

