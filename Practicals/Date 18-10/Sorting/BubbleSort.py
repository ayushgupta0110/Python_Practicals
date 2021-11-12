

def BubbleSort(arr):
    n= len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def main():
    print("\n\tBubble Sort")
    n = eval(input("Enter n :"))
    arr = []
    for i in range(n):
        arr.append(eval(input(f"Enter {i+1}th element: ")))

    BubbleSort(arr)
    print("Sorted array is: \n")
    for i in range(n):
        print(arr[i],end=" ")

if __name__ == '__main__':
    main()
