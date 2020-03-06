# Entrada
valor = int(input('Qual valor a sacar R$: '))

# Processamento
cem = valor // 100
resto = valor % 100

cinquenta = resto // 50
resto = resto % 50

vinte = resto // 20
resto = resto % 20

dez = resto // 10
resto = resto % 10

cinco = resto // 5
resto = resto % 5

dois = resto // 2

# Saída
resultado = '*** Seu Dinheiro ***'
resultado = resultado + f'\n{cem} x R$ 100'
resultado = resultado + f'\n{cinquenta} x R$ 50'
resultado = resultado + f'\n{vinte} x R$ 20'
resultado = resultado + f'\n{dez} x R$ 10'
resultado = resultado + f'\n{cinco} x R$ 5'
resultado = resultado + f'\n{dois} x R$ 2'
resultado = resultado + '\n*******************\n'

print(resultado)
