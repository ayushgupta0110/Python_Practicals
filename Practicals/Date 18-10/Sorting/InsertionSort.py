def InsertionSort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = temp;


def main():
    list = [12, 10, 34, 23, 11, 5, 7, 15]
    print(f"List Before Sort : {list}")
    InsertionSort(list)
    print(f"List After Sort : {list}")


if __name__ == '__main__':
    main()