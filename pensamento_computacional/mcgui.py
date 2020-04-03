
def fatorial(valor):
    # 5 * fatorial de 4
    if valor == 1:
        return 1
    else:
        r = valor * fatorial(valor-1)
        return r


print(fatorial(5))
