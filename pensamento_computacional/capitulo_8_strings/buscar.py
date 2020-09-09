from strings_utils_by_rs import contem, reverse


def main():
    frase = input('Frase: ')
    palavra = input('Palavra: ')

    # if contem(reverse(frase), palavra):
    if contem(frase, palavra):
        print('Sim. Palavra encontrada na frase')
    else:
        print('Não. A frase não contém a palavra')


main()
