def reverse(l) :

    res = []
    '''
    list.insert(i, elem)

    Here, elem is inserted to the list at the ith index. 
    All the elements after elem are shifted to the right.
    '''
    for i in l :
        res.insert(0, i)

    return res

list = [1, 2, 3, 4, 5]
rev = reverse(list)

print(f"Reverse of {list} is {rev}")