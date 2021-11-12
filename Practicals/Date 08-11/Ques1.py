def main():
    my_dict = dict()
    for i in range(1, 16):
        my_dict[i] = i ** 2

    for key in my_dict:
        print(f"{key} : {my_dict[key]}")


if __name__ == '__main__':
    main()
