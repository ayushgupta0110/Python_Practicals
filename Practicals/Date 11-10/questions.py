#   ques 10.4
print()

lst = [30, 1, 2, 1, 0]

print(lst.index(1))
print(lst.count(1))
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))

#   ques 10.3
print()

import random

lst = [30, 1, 2, 1, 0]

lst.append(40)
print(lst)

lst.insert(1, 43)
print(lst)

lst.extend([1, 43])
print(lst)

lst.remove(1)
print(lst)

lst.pop(1)
print(lst)

lst.pop()
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)

random.shuffle(lst)
print(lst)

#   ques 10.5
print()

list1 = [30, 1, 2, 1, 0]
list2 = [1, 21, 13]

print(list1 + list2)
print(list1[3])
print(2 * list2)
print(list2 * 2)
print(list1[1 : 3])

#   ques 10.6
print()

list1 = [30, 1, 2, 1, 0]

print([x for x in list1 if x > 1])
print([x for x in range(0, 10, 2)])
print([x for x in range(10, 0, -2)])

#   ques 10.7
print()

list1 = [30, 1, 2, 1, 0]
list2 = [1, 21, 13]

print(list1 < list2)
print(list1 <= list2)
print(list1 == list2)
print(list1 != list2)
print(list1 > list2)
print(list1 >= list2)