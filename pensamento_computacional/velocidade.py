# Leia uma velocidade em m/s, calcule e
# escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

# Entrada
velocidade_ms = int(input('Velocidade m/s: '))

# Processamento
velocidade_km = velocidade_ms * 3.6

# Saida
# print(f'{velocidade_ms} m/s é igual a {velocidade_km} km/h')
print('{} m/s é igual a {} km/h'.format(velocidade_ms, velocidade_km))
