def eh_multiplo(numero, alvo):
    if numero % alvo == 0:
        return True
    else:
        return False


def main():
    n = int(input('Número N: '))
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))

    while limite_inferior <= limite_superior:

        if eh_multiplo(limite_inferior, n):
            print(limite_inferior)

        limite_inferior = limite_inferior + 1

    print('Fim')


main()
