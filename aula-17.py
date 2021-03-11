num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 4')
#num.remove(2) # remove so um 2
#num.pop() # remove o ultimo
#num.pop(2)# remove o 0

#num = (2, 5, 9, 1)
#num[2] = 3 tuplas sao imutaveis
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}...')
print('cheguei ao final da lista.')
# ou list()

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}! ')
print('cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a[:] # faca uma copia dos valores de a
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')