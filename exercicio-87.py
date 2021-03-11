matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[c][l] = int(input(f'digite um valor para a matriz de coordenadas [{c}][{l}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'a soma dos valores e {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'a soma de todos os valores da terceira coluna e de {scol}')