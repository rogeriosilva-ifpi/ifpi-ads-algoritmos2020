def obter_inteiro(msg):
    try:
        valor = int(input(msg))
        return valor
    except:
        print('Valor Inválido!')
        return obter_inteiro(msg)


def obter_inteiro_positivo(msg):
    valor = obter_inteiro(msg)

    while valor <= 0:
        print('Vc deve digitar um inteiro positivo')
        valor = obter_inteiro(msg)

    return valor


def obter_string_tam_min(msg, tam):
    texto = input(msg)

    while len(texto) < tam:
        print(f'Deve ser maior que {tam} caracteres!')
        texto = input(msg)

    return texto
