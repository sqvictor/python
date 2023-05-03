pessoas = []
dados = []
leve = pesado = 0
mais = menos = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso em kg: ')))
    if len(pessoas) == 0:
        mais = menos = dados[1]
    else:
        if dados[1] > mais:
            mais = dados[1]
        if dados[1] < menos:
            menos = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = input('Deseja continuar? [S/N] ').strip()
    if r in 'Nn':
        break

for c in pessoas:
    if c[1] > 70:
        print(f'{c[0]} é pesado. Pesa {c[1]:.2f}kg.')
        pesado += 1
    else:
        print(f'{c[0]} é leve. Pesa {c[1]:.2f}kg.')
        leve += 1

print(f'O maior peso foi de {mais}kg. Peso de ', end='')
for c in pessoas:
    if c[1] == mais:
        print(f'{c[0]} ', end='')

print(f'\nTemos {leve} leves e {pesado} pesados.')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')