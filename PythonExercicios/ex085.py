# crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-se em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
num = []
pares = []
impares = []
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
num.append(pares[:])
num.append(impares[:])
print(f'A lista com todos os números é {num}')
print(f'Os números pares em ordem crescente: {pares}')
print(f'Os números ímpares em ordem crescente: {impares}')



