def max3(n1,n2,n3):
    def max2(n1,n2):

        if n1 > n2:
            return n1
        else:
            return n2

    return max2(max2(n1,n2),n3)

def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the Second  number: "))
    n3 = int(input("Enter the Third number: "))

    maximum = max3(n1,n2,n3)
    print('Maximum  number is', maximum)

if __name__=='__main__':
    main()