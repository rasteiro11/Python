s = c = 0
while True:
    n = int(input('digite um numero: '))
    c = c + 1
    if n == 999:
        break
    s = s + n
print(f'a soma deu um total de {s} e foram usados {c} numeros ')