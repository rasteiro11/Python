valor = int(input('que valor vocw quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= valor:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break