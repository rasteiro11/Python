from random import randint
lista = []
jogos = []
cont = 0
quant = int(input('Quantos jogos voce quer que eu sorteie?'))
tot = 1
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'sorteando {quant} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')


