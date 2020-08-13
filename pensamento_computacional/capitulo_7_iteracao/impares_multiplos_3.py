def main():
    qtd_multiplos = 0
    # inicializacao / estado inicial
    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    atual = inicio

    while atual <= fim:  # condic. de continuidade
        # trabalho
        if atual % 3 == 0 and atual % 2 != 0:
            qtd_multiplos = qtd_multiplos + 1
            print('>>>', atual)

        # convergencia do estado
        atual = atual + 1

    print(f'Foram encontrados {qtd_multiplos} números alvo.')


main()
