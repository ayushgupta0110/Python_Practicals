def sumDigits(n):
    sum=0
    res=0
    while(n>0):
        res = n % 10
        n = n // 10
        sum= sum + res
    return sum

def main():
    num = int(input("Enter the number: "))
    sum = sumDigits(num)
    print("Sum of Digits: ", sum)

if __name__ == '__main__':
    main()

