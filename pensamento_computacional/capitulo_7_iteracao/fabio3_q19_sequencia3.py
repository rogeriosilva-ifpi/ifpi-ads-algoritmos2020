def main():
    print('** Sequencia **')
    n = int(input('N: '))
    contador = 1
    valor = n
    s = 0

    while contador <= n:
        if contador % 2 == 0:
            s = s - (valor/contador)
        else:
            s = s + (contador/valor)

        valor -= 1
        contador += 1

    print(f'S = {s}')


main()
