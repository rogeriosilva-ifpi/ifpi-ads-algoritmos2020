def main():
    qtd = int(input('Quantos termos FIBO DYW? '))

    qtd_atual = 2
    anterior = 0
    atual = 1
    print(anterior, atual, end=' ')

    while qtd_atual < qtd:
        novo_atual = anterior + atual
        anterior = atual
        atual = novo_atual

        print(atual, end=' ')
        qtd_atual += 1

    print()


main()
