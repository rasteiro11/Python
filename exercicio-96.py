def area(larg, comp):
    a = larg * comp
    print(f'a area de um terreno {larg}X{comp} e de {a}')
while True:
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    area(l, c)
    continuar = str(input('Voce quer continuar? [S/N]'))
    if continuar not in 'Ss':
        break