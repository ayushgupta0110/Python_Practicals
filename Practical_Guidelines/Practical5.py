"""
5.Write a function that finds the sum of the n terms of the following series.
Import the factorial function created in question 4.
1–x^2/2!+x^4/4!–x^6/6!+...xn/n!
"""

from Practical3 import factorial


def sumOfSeries(x, n):
    sum = 0.0
    for i in range(0, 2 * n, 2):
        if i % 2 == 0:
            sum = sum + x ** i / factorial(i)
        else:
            sum = sum - x ** i / factorial(i)
    return sum


def main():
    print("Program to find the sum of the n terms of the following series")
    print("1–x^2/2!+x^4/4!–x^6/6!+...xn/n!\n")
    x = eval(input("Enter the value of x : "))
    n = eval(input("Enter value n for the series: "))
    for i in range(1, n+1):
        result = sumOfSeries(x, i)
        print(f"Sum of Series upto {i} terms : {result}")


if __name__ == '__main__':
    main()
