num = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')))
print(f'Voce digitou {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o vaalor 3 apareceu na {num.index(3)+1} posicao')
else:
    print(f'o valor 3 nao apareceu em nenhuma posicao')
print('os valores pares digitados foram: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')