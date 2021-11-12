def main():
    n = int(input('Enter height of triangle: '))

    for i in range(n + 1):
        for j in range(i):
            print('*', end=" ")
        print("")


if __name__== '__main__':
    main()