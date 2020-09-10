def main():
    # se nao achar o arquivo
    # https://stackoverflow.com/questions/49143852/trouble-opening-files-in-python-with-vs-code
    # "python.terminal.executeInFileDir": true,

    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


main()
