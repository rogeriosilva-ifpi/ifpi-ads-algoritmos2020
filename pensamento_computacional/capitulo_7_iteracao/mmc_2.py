def main():
    numero1 = int(input('N1: '))
    numero2 = int(input('N2: '))

    mmc = calcular_mmc(numero1, numero2)

    print('Achei...', mmc)


def calcular_mmc(numero1, numero2):
    maior = -1
    menor = -1

    if numero1 >= numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1

    mmc = menor
    while True:
        if mmc % maior == 0 and mmc % menor == 0:
            return mmc
        else:
            mmc = mmc + menor


main()
