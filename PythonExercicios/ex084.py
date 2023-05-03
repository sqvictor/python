# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas leves
pessoas = []
dados = []
leve = pesado = 0
while True:
    dados.append((str(input('Nome: '))))
    dados.append(float(input('Peso em kg: ')))
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
print(f'Temos {leve} leves e {pesado} pesados.')
