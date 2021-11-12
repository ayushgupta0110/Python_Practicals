def add(x, l = None) :

    if l == None :
        l = []

    if x not in l :
        l.append(x)

    return l

l1 = add(1)
print(l1)

l2 = add(2)
print(l1)

l3 = add(3, [1, 2, 3, 4, 5])
print(l3)

l4 = add(4)
print(l4)