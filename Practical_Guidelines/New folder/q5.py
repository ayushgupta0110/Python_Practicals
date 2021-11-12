from q3 import Factorial
'''
def fac(n) :
    
    prod = 1

    for i in range(1, n+1) :
        prod *= i

    return prod
'''
def sumSeries(n, x) :

    sum = 0

    for i in range(1, n+1) :

        if i%2 == 0 :
            sum += pow(x, 2*(i-1)) / Factorial(2*(i-1))

        else :
            sum -= pow(x, 2*(i-1)) / Factorial(2*(i-1))

    return sum

def main() :

    n = int(input("Enter limit : "))
    x = int(input("Enter value of 'x' : "))

    print(sumSeries(n, x))

main()