lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N]'))
    lista.sort(reverse=True)
    l = len(lista)
    if cont not in 'Ss':
        break
print(f'os numeros digitados foram {lista}')
print(f'o foram digitados {l} valores')
if 5 in lista:
    print('temos 5 na lista!')
