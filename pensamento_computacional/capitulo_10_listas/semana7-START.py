def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor (posição)'
    menu += '\n 3 - Mostrar Valor (todos)'
    menu += '\n 4 - Remover Valor (posição)'
    menu += '\n 5 - Atualizar Valor (posição)'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            # Listas quando passadas como argumentos e modificadas por
            # funções não é necessário retorná-las
            # Se modificar a lista dentro de um função, as variáveis que já
            # apontavam para ela terão acesso a lista moficiada normalmente
            # Por isso nao está ```lista = inserir_valores(lista)````
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            mostrar_todos(lista)
        elif opcao == 4:
            remover_valor(lista)
        elif opcao == 5:
            atualizar_valor(lista)
        elif opcao == 0:  # sair do while
            break
        else:
            print('Opção Inválida')

        input('<enter> to continue...')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir?'))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(f'Valor index[{posicao}] é {lista[posicao]}')


def mostrar_todos(colecao):
    tamanho = len(colecao)
    print(f'**** Mostrando {tamanho} valores ****')
    for valor in colecao:
        print(f'>> {valor}')


def remover_valor(valores):
    posicao = int(input('Qual posição vc quer remover? '))

    removido = valores.pop(posicao)
    print(f'O valor {removido} foi removido da posição {posicao}!')


def atualizar_valor(cesta):
    pos = int(input('Qual posição? '))

    valor = cesta[pos]
    print(f'Na posição {pos} existe atualmente o valor {valor}')

    novo_valor = int(input('Qual o novo valor? '))
    cesta[pos] = novo_valor
    print('Valor atualizado com sucesso!')


main()
