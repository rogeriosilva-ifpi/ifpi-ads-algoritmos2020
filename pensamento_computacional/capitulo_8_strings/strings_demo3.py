def main():
    nome = 'Rogério da Silva'
    novo_nome = ''

    for i in range(len(nome)-1, -1, -1):
        novo_nome += nome[i]

    print(nome)
    print(novo_nome)


main()
