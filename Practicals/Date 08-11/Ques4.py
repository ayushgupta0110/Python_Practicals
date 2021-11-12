# Write a Python program to combine two dictionary adding values for common keys.

from collections import Counter


def main():
    d1 = {'a': 300, 'b': 200, 'c': 200}
    d2 = {'a': 200, 'b': 100, 'd': 100}

    my_dict = Counter(d1) + Counter(d2)

    print(my_dict)


if __name__ == '__main__':
    main()
