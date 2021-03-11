m18 = m20 = m = idade = 0
while True:
    print('{:=^60}'.format(' CADASTRE UMA PESSOA '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: '))
    if sexo in 'Ff' and idade <20:
        m20 += 1
    if sexo in 'Mm':
        m += 1
    while sexo not in 'FfMm':
        sexo = str(input('Informação inválida, tente novamente[M/F]: '))
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        m18 += 1
    opc = str(input('Deseja continuar o cadastro [S/N]? '))
    while opc not in 'SsNn':
        opc = str(input('Resposta inválida, tente novamente[S/N]: '))
    print('=' * 60)
    if opc in 'Nn':
        break
print(f'''Pessoas maiores de 18 registradas: \033[32m{m18:>25}\033[m
Quantidade de homens registrados: \033[32m{m:>26}\033[m
Quantidade de mulheres abaixo dos 20 anos registradas: \033[32m{m20:>5}\033[m''')
print('='*60)
print('{:=^60}'.format(' FIM DO PROGRAMA '))
print('='*60)