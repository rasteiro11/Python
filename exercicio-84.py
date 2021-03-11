info = []
pessoas = []
continuar = ''
mai = men = 0
while True:
    info.append(str(input('Digite o seu nome: ')))
    info.append(float(input('Digite o seu peso: ')))
    if len(pessoas) == 0:
        mai = men = info[1]
    else:
        if info[1] > mai:
            mai = info[1]
        if info[1] < men:
            men = info[1]
    pessoas.append(info[:])
    info.clear()
    continuar = str(input('Deseja continuar? [S?N]'))
    if continuar not in 'Ss':
        break
print(f'os dados digitados foram {pessoas}')
print(f'ao todo foram {len(pessoas)} pessoas cadastradas')
print(f'o maior peso foi de {mai}')
print(f'o menor peso foi de {men}')
