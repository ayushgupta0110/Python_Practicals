"""
3. Write a Python function to find the nth term of Fibonacci sequence and its
factorial. Return the result as a list.
"""


def fibonacci(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = eval(input("Enter the value of n: "))
    my_list = [fibonacci(n), factorial(fibonacci(n))]
    print("The Nth term in fibonacci series and factorial of that nth term are : ", my_list)


if __name__ == '__main__':
    main()
