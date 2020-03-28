def main():
    salario = float(input('Renda: '))

    imposto = calcular_ir(salario)
    imposto_aj = calcular_ir_tabela_ajustada(salario)

    print(f'R$ {imposto:.2f}')


def calcular_ir(renda):

    imposto = 0.0

    # Acima de 4.664,68 (27,5%)
    if renda > 4664.68:
        renda_tributar = renda - 4664.68
        renda = 4664.68
        imposto += renda_tributar * (27.5/100)

    # De 3.751,06 até 4.664,68 (22,5%)
    if renda >= 3751.06:
        renda_tributar = renda - 3751.06
        renda = 3751.05
        imposto += renda_tributar * (22.5/100)

    # De 2.826,66 até 3.751,05 (15%)
    if renda >= 2826.66:
        renda_tributar = renda - 2826.65
        renda = 2826.65
        imposto += renda_tributar * (15/100)

    # De 1.903,99 até 2.826,65 (7,5%)
    if renda >= 1903.99:
        renda_tributar = renda - 1903.99
        renda = 1903.99
        imposto += renda_tributar * (7.5/100)

    return imposto


def calcular_ir_tabela_ajustada(renda):

    imposto = 0.0

    # Acima de 4.664,68 (27,5%)
    if renda > 4664.68:
        renda_tributar = renda - 4664.68
        renda = 4664.68
        imposto += renda_tributar * (27.5/100)

    # De 3.751,06 até 4.664,68 (22,5%)
    if renda >= 3751.06:
        renda_tributar = renda - 3751.06
        renda = 3751.05
        imposto += renda_tributar * (22.5/100)

    # De 2.826,66 até 3.751,05 (15%)
    if renda >= 2826.66:
        renda_tributar = renda - 2826.65
        renda = 2826.65
        imposto += renda_tributar * (15/100)

    # De 1.903,99 até 2.826,65 (7,5%)
    if renda >= 1903.99:
        renda_tributar = renda - 1903.99
        renda = 1903.99
        imposto += renda_tributar * (7.5/100)

    return imposto


if __name__ == '__main__':
    main()
