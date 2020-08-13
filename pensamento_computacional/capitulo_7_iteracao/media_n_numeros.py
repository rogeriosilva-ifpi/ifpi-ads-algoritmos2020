def main():
    contador = 0
    somatorio = 0
    qtd = 0
    numero = int(input('Número: '))

    while numero >= 0:
        somatorio = somatorio + numero
        qtd = qtd + 1
        numero = int(input('Número: '))

    # mostrar a média
    if qtd > 1:
        media = somatorio / qtd
        print('Média', media)


main()
