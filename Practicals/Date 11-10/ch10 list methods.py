#   APPEND

list1 = [2, 3, 4, 1, 32, 4]
list1.append(19)
print(list1)

#   COUNT

print(f"No. of occurences of 4 in {list1} is {list1.count(4)}")

#   EXTEND

list2 = [99, 54]
list1.extend(list2)
print(list1)

#   INDEX

print(list1.index(4))

#   INSERT

list1.insert(1, 25)
print(list1)

#   POP

list3 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]

list3.pop(2)
print(list3)

list3.pop()
print(list3)

#   REMOVE

list3.remove(32)
print(list3)

#   SORT and REVERSE

list3.reverse()
print(list3)

list3.sort()
print(list3)