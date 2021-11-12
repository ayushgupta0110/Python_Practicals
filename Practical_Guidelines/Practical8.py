"""
8. Write a Python program to perform the following using list:
a) Check if all elements in list are numbers or not.
b) If it is a numeric list, then count number of odd values in it.
c) If list contains all Strings, then display largest String in the list.
d) Display list in reverse form.
e) Find a specified element in list.
f) Remove the specified element from the list.
g) Sort the list in descending order.
h) Accept 2 lists and find the common members in them
"""


def check_numeric(ls):
    for i in ls:
        if type(i) != type(0):
            return False
    return True


def count_odd(ls):
    counter = 0
    for i in ls:
        if i % 2 != 0:
            counter += 1
    return counter


def check_str(ls):
    for i in ls:
        if type(i) != type(" "):
            return False
    return True


def max_str(ls):
    return max(ls, key=len)


def reverse_ls(ls):
    return ls.reverse()


def find_ls(ls, element):
    if element in ls:
        return True
    return False


def rm(ls, element):
    if element in ls:
        ls.remove(element)
    else:
        print("Element not present in List")


def sort(ls):
    ls.sort(reverse=True)


def find_common(l1, l2):
    common_ls = []
    for element in l1:
        if element in l2:
            common_ls.append(element)
    return common_ls


def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = ['hi', 'hello', 'Good', "bye", 'python']
    l3 = ['hello', 'bye', 'python', '10']

    if check_numeric(l1):
        print("L1 has all elements numbers")
        print("Odd numbers = ", count_odd(l1))

    if check_str(l2):
        print("L2 has all elements string")
        print("Max string = ", max_str(l2))

    to_find = 'bye'
    if (find_ls(l3, to_find)):
        print(f"Element '{to_find}' found in list")
    else:
        print(f"Element '{to_find}' not found in list")

    to_remove = '10'
    rm(l3, to_remove)
    print("Modified L3 = ", l3)

    common = find_common(l3, l2)
    print("Common elements in l2 and l3 = ", common)

    l1.reverse()
    print("Reverse List L1: ", l1)


if __name__ == "__main__":
    main()
