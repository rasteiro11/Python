lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    continuar = str(input('Quer continuar ? [S/N]'))
    if continuar not in 'Ss':
        break
print(f'A lista de Pares {lista_par};A lista de Impares {lista_impar} ;A lista inteira {lista}')