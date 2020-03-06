# Entrada
num = int(input('Número de 3 dígitos\n>>> '))

# Processamento
c = num // 100
resto = num % 100
d = resto // 10
u = resto % 10

# inverso = f'{u}{d}{c}'
inverso = u*100 + d*10 + c

# Saída
print(inverso)
