pergunta = "S"
contador = somador = maior = menor = 0
while pergunta == "S":
    numero = int(input('Digite um número: '))
    contador += 1
    somador += numero
    pergunta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while pergunta != "S" and pergunta != "N":
        print('COMANDO INVÁLIDO!')
        pergunta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f'Você digitou {contador} números, e a média foi {somador / contador:.1f}.')
print(f'O maior valor foi o {maior}, e o menor valor foi o {menor}.')