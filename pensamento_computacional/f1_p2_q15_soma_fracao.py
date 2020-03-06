# Entrada
num1 = int(input('Numerador 1: '))
dem1 = int(input('Denominador 1: '))

num2 = int(input('Numerador 2: '))
dem2 = int(input('Denominador 2: '))

# Processamento
dem = dem1 * dem2
num = (dem / dem1)*num1 + (dem / dem2)*num2

# Saída
print('Soma: {:.0f}/{:.0f}'.format(num, dem))
