# 6. Consider a tuple t1 ={1,2,5,7,9,2,4,6,8,1 0}.
# Write a program to perform following operations:
# a) Print another tuple whose values are even numbers in the given tuple.
# b) Concatenate a tuple t2={1 1 ,1 3,1 5) with t1 .
# c) Return maximum and minimum value from this tuple.

def main():
    t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
    my_list = []
    for x in t1:
        if x & 1 == 0:
            my_list.append(x)
    t2 = tuple(my_list)
    print("Tuple containing even numbers: ", t2)

    # concatenation
    t2 = (11, 12, 13)
    l1 = list(t1)
    l2 = list(t2)
    l1.extend(l2)
    t3 = tuple(l1)
    print("Concatenated tuple: ", t3)

    # max and min elements
    l1 = list(t1)
    my_max = max(l1)
    my_min = min(l1)
    print("Maximum element in tuple ", t1, " is: ", my_max)
    print("Minimum element in tuple ", t1, " is: ", my_min)


if __name__ == '__main__':
    main()
