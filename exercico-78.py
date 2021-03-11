lista = []
for c in range(0, 5):
    lista.append(int(input(f'digite o {c} valor da lista')))
print(lista)
lista.sort()
print(f'O maior valor e {lista[4]}')
print(f'o menor valor da lista e {lista[0]}')

#######################################################################

valores = [int(input('Digite o valor para a posição {}: '.format(i))) for i in range(5)]
print('=-' * 30)
print('Você digitou os valores {}: '.format(valores))

maior = max(valores)
menor = min(valores)

print('O maior valor digitado foi o {} nas posições '.format(maior), end='')
for ind, val in enumerate(valores):
    if val == maior:
        print(f'{ind}...', end='')

print('\nO menor valor digitado foi o {} nas posições '.format(menor), end='')
for ind, val in enumerate(valores):
    if val == menor:
        print(f'{ind}...', end='')

#######################################################################

valores = []
maior = 0
menor = 0
posicoesMaior = []
posicoesMenor = []

for i in range(0, 5):
    numero = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(numero)

    if i == 0:
        maior = menor = valores[i]
    elif valores[i] > maior:
        maior = valores[i]
    elif valores[i] < menor:
        menor = valores[i]

for i in range(0, 5):
    if valores[i] == maior:
        posicoesMaior.append(i)
    if valores[i] == menor:
        posicoesMenor.append(i)

print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao in posicoesMaior:
    print(posicao, end='... ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for posicao in posicoesMenor:
    print(posicao, end='... ')
print()