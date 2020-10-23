
import os
import json


def main():
    # lista de vagas
    nome_arquivo = 'jobs.bd'
    vagas = inicializar(nome_arquivo)

    menu = tela_principal()
    opcao = int(input(menu))

    # Loop da Tela Principal
    while opcao != 0:

        if opcao == 1:
            vaga = nova_vaga()
            vagas.append(vaga)
        elif opcao == 2:
            renderVarias(vagas)

        input('<enter> para continuar...')
        opcao = int(input(menu))

    finalizar(nome_arquivo, vagas)


# ***** VIEWS *******
def tela_principal():
    menu = '******* Jobs App ********\n'
    menu += '1 - Nova Vaga\n'
    menu += '2 - Listar todas\n'
    menu += '0 - Sair do App\n'
    menu += '\nopção >>> '

    return menu


def renderVarias(vagas):
    """ Exibe na tela uma lista de vagas recebida """
    qtd = len(vagas)
    print('*** Vagas Cadastradas ***')
    print(f'>> {qtd} vagas encontradas: ')

    for vaga in vagas:
        print(10*'---')
        render(vaga)

    print(10*'===')


def render(vaga):
    """ Exibe na tela a Vaga recebida """
    # vaga é um dict, for i in dict, será for nas chaves do dict
    for chave in vaga:
        print(f'\t{chave.capitalize()}:', vaga[chave])


# ****** ARQUIVO ******

def inicializar(nome_arquivo):
    """
        Verifica se existe um arquivo no diretório corrente,
        se existe carrega os dados em json dele,
        senao retorna uma lista vazia
    """
    vagas = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo)

        # todos os dados estarão em json e em apenas uma linha
        dados = arquivo.readline()
        arquivo.close()
        if dados:
            vagas = json.loads(dados)

    return vagas


def finalizar(nome_arquivo, vagas):
    """
        Gravas no arquivo 'nome_arquivo' as Vagas recebidas, no formato json
    """

    dados = json.dumps(vagas)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


# ****** VAGAS ******

def nova_vaga():
    print('Forneça os dados na Nova Vaga')
    descricao = input('Descricão: ')
    remoto = input('Remoto? ')
    ingles = input('Ingles? ')
    salario = float(input('Salário: '))
    tech = input('Tecnologias: ')
    contratacao = input('Forma de Contratacao (PJ | CLT): ')

    vaga = {
        'descricao': descricao,
        'remoto': remoto,
        'ingles': ingles,
        'salario': salario,
        'tech': tech,
        'contratacao': contratacao
    }

    return vaga


if __name__ == '__main__':
    main()
