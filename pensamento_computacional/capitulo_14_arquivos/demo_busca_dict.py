import os
from input_utils import obter_inteiro, obter_string_tam_min, obter_inteiro_positivo


def main():
    menu = '** Países **\n'
    menu += '1 - add\n'
    menu += '2 - list\n'
    menu += '3 - search\n'
    menu += '\nop >> '

    op = int(input(menu))

    paises = []

    while op != 0:
        if op == 1:
            # add
            nome = obter_string_tam_min('Nome: ', 3)
            continente = obter_string_tam_min('Continuente: ', 5)
            populacao = obter_inteiro_positivo('População (M): ')
            pais = {'nome': nome, 'continente': continente,
                    'populacao': populacao}
            paises.append(pais)
        elif op == 2:
            # list
            print('Lista de Países cadastrados: ')
            for pais in paises:
                show_pais(pais)
        elif op == 3:
            # search
            print('Pesquisa por parte do nome')
            q = input('Pesquisa: ')
            paises_encontrados = pesquisar_por_parte_nome(paises, q)
            for pais in paises_encontrados:
                show_pais(pais)

        else:
            print('Opção inválida!')

        input('<enter>..')
        os.system('clear')
        op = op = int(input(menu))


def show_pais(pais):
    print('Nome:', pais['nome'])
    print('Cont:', pais['continente'])
    print('População (M):', pais['populacao'])
    print('--------------------------')


def pesquisar_por_parte_nome(paises, chave_busca):
    resultado = []

    for pais in paises:
        if chave_busca.upper() in pais['nome'].upper():
            resultado.append(pais)

    return resultado


main()
