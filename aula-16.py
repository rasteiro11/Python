lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(lanche[cont])
#for comida in lanche:
    #print(f'eu vou comer {comida}')
#print('comi pra caramba')

#tuplas sao imutaveis
#lanche[1] = 'Refrigerantes'
print(lanche[1])
print(lanche[1:3])
print(lanche[-1])

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}na posicao {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao')

print(sorted(lanche))
print(lanche)

a = (2, 3, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))
print(c.index(5))

pessoa = ('Gustavp', 39, 'M', 99.8)
print(pessoa)

