def displayPattern(n):
    # number of spaces
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in reversed(range(i+1)):
            # printing stars
            print( j+1, end=" ")
        print("\r")

def main():
    n=int(input("Enter value of n: "))
    displayPattern(n)

if __name__ == '__main__':
    main()

