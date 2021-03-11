from random import randint
v = 0
while True:
    j = int(input('Digite um numero: '))
    c = randint(0, 10)
    total = j + c
    Par_Impar = ' '
    while Par_Impar not in 'PI':
        Par_Impar = str(input('Par ou Impar ? [P/I]')).strip().upper()[0]
    print(f'voce jogou {j} e o computador jogou {c}. Total de {total}')
    if Par_Impar == 'P':
        if total % 2 == 0:
            print('voce venceu!')
            v += 1
        else:
            print('voce perdeu')
            break
    elif Par_Impar == 'I':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    print('Vamos joagar novamente... ?')
print(f'Game Over. voce venceu {v} vezes')