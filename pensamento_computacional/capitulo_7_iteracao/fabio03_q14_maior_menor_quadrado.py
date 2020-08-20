def programa():
    n = int(input('N: '))
    numero = 1

    while numero ** 2 <= n:
        quadrado = numero * numero
        numero += 1

    print(quadrado)


programa()
