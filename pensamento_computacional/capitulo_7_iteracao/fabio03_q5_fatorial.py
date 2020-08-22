def programa():
    numero = int(input('Número: '))
    fatorial = 1

    while numero >= 1:
        fatorial = fatorial * numero
        numero = numero - 1

    print('Fatorial', fatorial)


programa()
