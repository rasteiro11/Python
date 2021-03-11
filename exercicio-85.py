par = []
impar = []
for rep in range(0, 7):
    n = int(input('Digite um valor numerico: '))
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
        impar.append(n)
        impar.sort()
print(par)
print(impar)
##############################################################
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'os numeros pares em ordem crescente sao {num[0]}')
print(f'os numeros impares em ordem crescente sao {num[1]}')
