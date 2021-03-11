cont = 0
while True:
    tab = int(input('voce quer a tabuada de que numero: '))
    while True:
        print(f'{tab} X {cont} = {tab*cont}')
        cont = cont + 1
        if cont > 10:
            cont = 0
            break