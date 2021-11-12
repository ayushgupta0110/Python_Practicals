# Write a function that takes a number (>=1 0) as an input and return the digits of
# the number as a set

def returnDigits(n):
    my_list = []
    while n != 0:
        x = n % 10
        my_list.append(x)
        n = n // 10
    my_set = set(my_list)
    return my_set


def main():
    n = eval(input("Enter a number(>=10): "))
    if n < 10:
        print("Please enter a valid number(>=10)")
        return
    else:
        my_set = returnDigits(n)
        print(my_set)


if __name__ == '__main__':
    main()
