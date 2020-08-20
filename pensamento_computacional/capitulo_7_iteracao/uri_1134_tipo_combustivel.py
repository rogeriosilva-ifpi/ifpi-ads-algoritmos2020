def main():
    alcool = 0
    gasolina = 0
    diesel = 0

    codigo = int(input('Código: '))

    while codigo != 4:
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1

        codigo = int(input('Código: '))

    # apresentar o resultad
    print('MUITO OBRIGADO')
    print('Alcool:', alcool)
    print('Gasolina:', gasolina)
    print('Diesel:', diesel)


main()
