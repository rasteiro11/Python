###lista = []
#while True:
   # cont = str(input('Voce quer adicionar um novo valor [S/N]?'))
   # if cont in 'Ss':
    #    lista.append(int(input(f'Digite um valor para ser adicionado na lista:')))
     #   if
   # if cont not in 'Ss':
    #    break
###print(lista)
########################################################################################
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if  n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'voce digitou os valores {numeros}')
