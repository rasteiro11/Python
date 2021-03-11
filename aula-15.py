cont = 1
while cont <= 10:
    print(cont, '-> ',end='')
    cont += 1
print('acabou')

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
#print('a soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'jose'
idade = 33
print(f'o nome {nome} tem {idade} anos')
print('o nome {} tem {} anos'.format(nome, idade))
print('o %s tem %d anos' % (nome, idade))

salario = 987.35
print(f'o {nome:^20} tem {idade} anos e ganha R${salario:.2f}')