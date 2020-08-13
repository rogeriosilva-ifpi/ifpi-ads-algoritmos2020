def main():
    numero1 = int(input('N1: '))
    numero2 = int(input('N2: '))

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
            print('Achei...', mmc)
            break
        else:
            mmc = mmc + menor


main()
