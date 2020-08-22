def main():
    n = int(input('N: '))
    numerador = 1
    somatorio = 0

    while n >= 1:
        somatorio += numerador/n
        n = n - 1
        numerador = numerador + 1

    print(somatorio)


main()
