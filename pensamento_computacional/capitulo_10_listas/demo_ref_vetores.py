def main():
    numeros = [1, 2, 5, 6]

    dobrar_valores(numeros)

    print(numeros)


def dobrar_valores(vetor):
    for i in range(len(vetor)):
        vetor[i] = vetor[i] * 2


main()
