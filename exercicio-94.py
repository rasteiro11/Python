cadastro = []
pessoa = {}
idades = f = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Responda apenas N ou S.')
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    cadastro.append(pessoa.copy())
    if pessoa['sexo'] in 'F':
        f = 1
    resp = str(input('Quer continuar? [S/N] '))
    while resp not in 'SsNn':
        print('ERRO! Responda apenas N ou S.')
        resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'- O Grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {idades / len(cadastro):.2f} anos.')
if f == 0:
    print('- Nenhuma mulher foi cadastrada.', end='')
else:
    print('- As mulheres cadastradas foram: ', end='')
    for m in range(0, len(cadastro)):
        if cadastro[m]['sexo'] in 'F':
            print(f' {cadastro[m]["nome"]} ', end='')
if len(cadastro) > 1:
    print('\n- Lista de pessoas acima da média: ')
    for i, v in enumerate(cadastro):
        if cadastro[i]['idade'] > (idades / len(cadastro)):
            for k, r in cadastro[i].items():
                print(f'  {k} = {r};', end='')
            print()