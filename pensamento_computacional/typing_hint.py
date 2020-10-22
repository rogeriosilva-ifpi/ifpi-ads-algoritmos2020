def main():
    # r = soma(1, 2)
    # print(r)


def soma(*args) -> int:
    r = sum(args)
    if r:
        return r


main()
