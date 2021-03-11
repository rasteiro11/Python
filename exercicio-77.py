palavras = ('AVIÃO', 'CARRO' , 'FUTEBOL', 'SKATE','PYTHON','JAVA','CHUVA','ARVORE','NATUREZA')
for p in palavras:
    print(f'\na palavra {p.upper()} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')