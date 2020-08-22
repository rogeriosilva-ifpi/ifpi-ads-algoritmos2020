def main():
    n = int(input('N: '))
    num = 1
    somatorio = 0

    while num <= n:
        somatorio = somatorio + 1/num
        num = num + 1

    print(somatorio)


main()
