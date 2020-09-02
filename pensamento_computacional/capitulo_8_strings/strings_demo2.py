def main():
    nome = 'Rogério da Silva'
    novo_nome = ''

    for i in range(len(nome)):
        if i % 2 != 0:
            novo_nome = novo_nome + '*'
        else:
            novo_nome = novo_nome + nome[i]

    print(nome)
    print(novo_nome)


main()
