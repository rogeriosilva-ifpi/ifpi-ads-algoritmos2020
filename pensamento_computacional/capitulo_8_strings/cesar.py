def main():
    mensagem = input('Mensagem: ')
    chave = obter_numero_positivo('Chave: ')

    mensagem_criptografada = cripto_cesar(mensagem, chave)

    print(f'Mensagem encriptada: {mensagem_criptografada}')


def cripto_cesar(texto, key):
    texto_encriptado = ''
    for caractere in texto:
        if eh_letra(caractere):
            novo_caractere = rotacionar_caractere(caractere, key)
            texto_encriptado += novo_caractere
        else:
            texto_encriptado += caractere

    return texto_encriptado


def rotacionar_caractere(c, k):
    codigo = ord(c)
    novo_codigo = codigo + k
    if (eh_letra_maiuscula(c) and novo_codigo > 90)\
            or (eh_letra_minuscula(c) and novo_codigo > 122):
        novo_codigo -= 26

    novo_caractere = chr(novo_codigo)
    return novo_caractere


def eh_letra_maiuscula(c):
    return ord(c) >= 65 and ord(c) <= 90


def eh_letra_minuscula(c):
    return ord(c) >= 97 and ord(c) <= 122


def eh_letra(c):
    # return eh_letra_maiuscula(c) or eh_letra_minuscula(c)
    if eh_letra_maiuscula(c) or eh_letra_minuscula(c):
        return True
    else:
        return False


def obter_numero_positivo(msg):
    num = int(input(msg))

    while num < 1:
        num = int(input('Valor incorreto! ' + msg))

    return num


main()
