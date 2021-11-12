# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum


def main():
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum of all values in dictionary :", returnSum(dict))


if __name__ == '__main__':
    main()
