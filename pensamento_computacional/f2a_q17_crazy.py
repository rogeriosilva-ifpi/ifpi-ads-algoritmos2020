# Leia valores inteiros em duas variáveis distintas e
# se o resto da divisão da primeira pela segunda for 1 escreva a
# soma dessas variáveis mais o resto da divisão;
# se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares;
# se for igual a 3 multiplique a soma dos valores lidos pelo primeiro;
# se for igual a 4 divida a soma dos números lidos pelo segundo,
# se este for diferente de zero. Em qualquer outra situação escreva o
# quadrado dos números lidos.

valor1 = 1343
valor2 = 765756

resto = valor1 % valor2

if resto == 1:
    # faca isso
    resultado = valor2 + valor1 + resto
    print(resultado)
elif resto == 2:
    # fazer outra coisa
    if valor1 % 2 == 0:
        print('Valor 1 é par')
    else:
        print('Valor 1 é ímpar')

    if valor2 % 2 == 0:
        print('Valor 2 é par')
    else:
        print('Valor 2 é ímpar')
elif:
    pass
else:
    # quadrado de cad aum valores
