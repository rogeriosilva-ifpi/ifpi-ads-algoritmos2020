def main():
    tipo = input('file | alcatra | picanha: ')
    qtd = int(input('Kg: '))

    valor_total = calcular_valor_total(tipo, qtd)

    eh_no_cartao = input('É no cartao S | N: ')
    desconto = calcular_desconto(eh_no_cartao, valor_total)

    valor_a_pagar = valor_total - desconto

    imprimir_cupom_fical(tipo, qtd, valor_total,
                         eh_no_cartao, desconto, valor_a_pagar)


def calcular_valor_total(tipo, qtd):
    if tipo == 'file':
        if qtd <= 5:
            valor_total = 4.90 * qtd
        else:
            valor_total = 5.80 * qtd
    elif tipo == 'alcatra':
        if qtd <= 5:
            valor_total = 5.90 * qtd
        else:
            valor_total = 6.80 * qtd
    else:
        if qtd <= 5:
            valor_total = 6.90 * qtd
        else:
            valor_total = 7.80 * qtd

    return valor_total


def calcular_desconto(cartao, valor_total):
    desconto = 0

    if cartao == 'S':
        desconto = valor_total * (5/100)

    return desconto


def imprimir_cupom_fical(tipo, qtd, valor_total, eh_no_cartao, desconto, valor_a_pagar):
    print(6 * '#', ' - CUPOM FISCAL - ', 6 * '#')
    print(f'Carne: {tipo}')
    print(f'Kg: {qtd}')
    print(f'Valor Total R$ {valor_total}')
    print(f'É no cartão? {eh_no_cartao}')
    print(f'Desconto R$ {desconto}')
    print(30 * '-')
    print(f'Valor a pagar: R$ {valor_a_pagar}')


main()
