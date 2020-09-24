def main():
    tamanho = int(input('Quantos Números? '))

    vetor = gerar_vetor(tamanho, -1)

    print(vetor)
    for pos in range(tamanho):
        valor = int(input(f'Número {pos}: '))
        vetor[pos] = valor

    print(vetor)

    # obter infos
    mostrar_info(vetor)

    vetor_transformado = transformar(vetor)
    print('Vetor Transformado')
    print(vetor)

    mostrar_info(vetor_transformado)

    media = calcular_media(vetor_transformado)

    print(f'\nMédia dos Valores: {media}')


def mostrar_info(vetor):
    qtd_pares = contar_pares(vetor)
    qtd_impares = contar_impares(vetor)
    qtd_positivos = contar_positivos(vetor)
    qtd_negativos = contar_negativos(vetor)

    print(f'Pares: {qtd_pares}')
    print(f'Ímpares: {qtd_impares}')
    print(f'Positivos: {qtd_positivos}')
    print(f'Negativos: {qtd_negativos}')


def gerar_vetor(tam, valor_padrao):
    return [valor_padrao] * tam


def contar_pares(vetor):
    qtd = 0
    for numero in vetor:
        if numero % 2 == 0:
            qtd += 1

    return qtd


def contar_impares(vetor):
    qtd = 0
    for numero in vetor:
        if numero % 2 != 0:
            qtd += 1

    return qtd


def contar_positivos(vetor):
    qtd = 0
    for n in vetor:
        if n > 0:
            qtd += 1

    return qtd


def contar_negativos(vetor):
    qtd = 0
    for n in vetor:
        if n < 0:
            qtd += 1

    return qtd


def transformar(vetor):
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = vetor[i] * 2
        else:
            vetor[i] = vetor[i] / 2

    return vetor


def calcular_media(vetor):
    somatorio = 0
    for valor in vetor:
        somatorio += valor

    media = somatorio / len(vetor)

    return media


main()
