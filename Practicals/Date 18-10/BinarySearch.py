def binarySearch(lst,key):
    low=0
    high = len(lst)-1

    while high>=low:
        mid=(low+high)//2
        if key < lst[mid]:
            high = mid-1
        elif key == lst[mid]:
            return mid
        else:
            low = mid+1

    return -low -1

def main():
    lst = [2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79]
    i = binarySearch(lst, 2)
    print(i)
    j = binarySearch(lst, 11)
    print(j)
    k = binarySearch(lst, 12)
    print(k)
    l = binarySearch(lst, 1)
    print(l)
    m = binarySearch(lst, 3)
    print(m)

if __name__ == '__main__':
    main()

