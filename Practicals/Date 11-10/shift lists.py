def shift(lst):

    temp = lst[0] # Retain the first element

    # Shift elements left
    for i in range(1, len(lst)):
        lst[i - 1] = lst[i]

    # Move the first element to fill in the last position
    lst[len(lst) - 1] = temp

list = [2, 3, 4, 9, 1, 0, 7]

shift(list)
print(list)