def main():
    qtd = int(input('Quantas fichas? '))
    id_magro = -1
    id_gordo = -1
    peso_magro = -1
    peso_gordo = -1

    for i in range(qtd):
        print(f'---- Dados da Ficha {i+1} ---')
        id = input('Identificação: ')
        nome = input('Nome: ')
        peso = float(input('Peso (kg): '))

        if i == 0:  # se primeira ficha
            id_magro = id
            id_gordo = id
            peso_magro = peso
            peso_gordo = peso
        else:  # a partir da segunda ficha
            if peso < peso_magro:
                id_magro = id
                peso_magro = peso

            if peso > peso_gordo:
                id_gordo = id
                peso_gordo = peso

        print()
    # apresentar os resultados
    print('**** RESULTADO ****')
    print(f'Boi mais Magro id:{id_magro} - peso {peso_magro} kg')
    print(f'Boi mais Gordo id:{id_gordo} - peso {peso_gordo} kg')


main()
