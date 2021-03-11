from random import randint
numeros = []
lista_vazia = []
c = 0


def sorteio(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(lista)


def somapar(lista, lista_par, cont):
    for i in range(0, 5):
        if lista[i] % 2 == 0:
            lista_par.append(lista[i])
            cont += lista[i]
    print(lista_par)
    print(c)


sorteio(numeros)
somapar(numeros, lista_vazia, c)





