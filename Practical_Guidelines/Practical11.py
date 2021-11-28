"""
11. Write a menu-driven program to accept a list of student names and perform
    the following:
    a. search an element using linear search/ binary search.
    b. Sort the elements using bubble sort/ insertion sort/ selection sort.
"""
def BubbleSort(lst):
    ln = len(lst)
    for i in range(ln-1):
        for j in range(ln-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
        
def InsertionSort(lst):
    ln = len(lst)
    for i in range(1,ln):
        temp = lst[i]
        j = i-1
        while j>=0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = temp

def SelectionSort(lst):
    ln = len(lst)
    for i in range(ln-1):
        minj = i
        for j in range(i,ln):
            if lst[minj] > lst[j]:
                minj = j
        temp = lst[i]
        lst[i] = lst[minj]
        lst[minj] = temp
            
        
def LinearSearch(lst,el):
    for i in range(len(lst)):
        if(lst[i] == el):
            return i
    return -1
    
def BinarySearch(lst,el):
    last = len(lst)
    start = 0
    while(start <= last):
        mid = (start + last)//2
        if el == lst[mid]:
            return mid
        elif el < lst[mid]:
            last = mid - 1
        else:
            start = mid + 1
    return -1
            

def SortMenu(lst):
    ch = 1
    while ch != 0:
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            BubbleSort(lst)
            ch = 0
        elif choice == 2:
            InsertionSort(lst)
            ch = 0
        elif choice == 3:
            SelectionSort(lst)
            ch = 0
        else:
            print("!!wrong choice try again...")
            ch = 1
    print("list sorted successfully.")
    print(lst)

def SearchMenu(lst):
    ch = 1
    while ch != 0:
        print("1. Linear Search")
        print("2. Binary Search")
        choice = int(input("Enter your choice : "))
        el = input("Enter the name to search in list : ")
        if choice == 1:
            index = LinearSearch(lst,el)
            if index == -1:
                print(el," not found in list ")
            else:
                print(el," found in list at index ",index)
            ch = 0
        elif choice == 2:
            #checking for sorted list
            for i in range(len(lst)-1):
                if lst[i] > lst[i+1]:
                    print("error!! list is not sorted")
                    exit(1)
            
            index = BinarySearch(lst,el)
            if index == -1:
                print(el," not found in list ")
            else:
                print(el," found in list at index ",index)
            ch = 0
        else:
            print("!!wrong choice try again...")
            ch = 1
            continue
        
def main():
    lst = []
    n = int(input("Enter the no. of Students : "))
    print("Enter the student name : ")
    for i in range(n):
        lst.append(input())
    ch = 1   
    while ch != 0:
        print("1. Sort List")
        print("2. Search in List")
        choice = int(input("Enter your choice : "))
        print()
        if choice == 1:
            SortMenu(lst)
        elif choice == 2:
            SearchMenu(lst)
        else:
            print("!!wrong choice try again...")
            ch = 1
            continue
        
        ch = int(input("Do you want to continue (1/0) : "))
        print()
            
if __name__ == "__main__":
    main()