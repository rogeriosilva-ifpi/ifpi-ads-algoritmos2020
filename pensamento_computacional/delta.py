# import ferramentas
# from ferramentas import calcular_delta
from ferramentas import calcular_delta as d


def main():
    print('*** DELTA ***')
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))

    # d = ferramentas.calcular_delta(a, b, c)
    r = d(a, b, c)

    print(f'O Delta é {r}')


# def calcular_delta(a, b, c):
#     delta = b**2 - 4*a*c
#     return delta


main()
