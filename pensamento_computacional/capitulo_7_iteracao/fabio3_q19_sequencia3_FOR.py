def main():
    print('** Sequencia **')
    n = int(input('N: '))
    s = 0

    for contador in range(1, n+1, 1):
        if contador % 2 == 0:
            s = s - ((n-contador+1)/contador)
        else:
            s = s + (contador/(n-contador+1))

    print(f'S = {s}')


main()
