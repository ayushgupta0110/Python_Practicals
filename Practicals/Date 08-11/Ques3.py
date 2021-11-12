def main():
    fruits = ['mango', 'pear', 'apple', 'papaya']
    price = [90, 78, 110, 60]

    fruits_price = zip(fruits, price)

    # create dictionary
    fruits_dict = {}

    for key, value in fruits_price:
        if key in fruits_dict:  # handling duplicate keys
            pass
        else:
            fruits_dict[key] = value

    print(fruits_dict)


if __name__ == '__main__':
    main()
