def lin():
    print('-' * 30)

lin()
print(' CURSO EM VIDEO  ')
lin()
print(' APRENDA PYTHON  ')
lin()
print(' GUSTAVO GUANABARA  ')
lin()

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-'*30)

titulo(' CURSO EM VIDEO ')
titulo(' PYTHON E MUITO BOM! ')
titulo(' Oi ')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(b=4, a=5)
#s = a + b
#print(s)
soma(8, 9)
#s = a + b
#print(s)
soma(2, 1)
#s = a + b
#print(s)

def contador(* num):
    for valor in num:
        print(f'{valor}',end='')
    print('FIM')

contador(2 ,1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(* num):
    tam  = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros ')

contador(2 ,1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s = num + s
    print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 9, 4)