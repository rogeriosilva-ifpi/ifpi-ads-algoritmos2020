def main():
    # arq = open('frutas.txt', 'r')
    ''' 
        1 - add
        2 - edit
        3 - remove
        4 - list
        5 - show
        0 - quit
    '''
    frutas = []

    # salvar em bd
    arq = open('frutas.txt', 'r')

    for linha in arq:
        frutas.append(linha.strip())

    arq.close()

    # show
    print(frutas)


main()
