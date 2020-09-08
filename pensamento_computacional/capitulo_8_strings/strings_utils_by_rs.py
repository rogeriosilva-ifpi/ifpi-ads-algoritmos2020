def contem(frase, palavra):
    """
        frase: o rato roeu a roupa do rei de roma
        palavra: rei
    """
    tam_frase = len(frase)
    tam_palavra = len(palavra)
    for pos in range((tam_frase-tam_palavra)+1):
        # print(f'Fatia começando em "{frase[pos]}"')
        fatia = substring(frase, pos, tam_palavra)
        if fatia == palavra:
            return True

    return False


def substring(frase, pos, tamanho):
    """
        frase: 'Joaquim venceu o Jogo.', 'roma'
        pos: 3, 0
        tamanho: 4, 4
        return: 'quim', 'roma'
    """
    fatia = ''
    for i in range(pos, pos+tamanho):
        fatia += frase[i]

    return fatia


def reverse(texto):
    retorno = ''
    for i in range(len(texto)-1, -1, -1):
        retorno += texto[i]

    return retorno
