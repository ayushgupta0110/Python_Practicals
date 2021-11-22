def main():
    while True:
        try:
            filename = input("Enter a filename: ").strip()
            fn = open(filename, 'r')
            fn1 = open('output.txt', 'w')
            break
        except IOError:
            print("File " + filename + "does not exist! Please try again.")

    # read the content of the file line by line
    cont = fn.readlines()
    type(cont)
    for i in range(0, len(cont)):
        if (i+1) % 2 != 0:
            fn1.write(cont[i])
        else:
            pass

    fn1.close()

    # open file in read mode
    try:
        fn1 = open('output.txt', 'r')
    except IOError:
        print("File output.txt does not exist! Please try again.")

    # read the content of the file
    cont1 = fn1.read()

    # print the content of the file
    print(cont1)

    fn.close()
    fn1.close()


if __name__ == '__main__':
    main()
