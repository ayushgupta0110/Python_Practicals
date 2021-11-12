import random

#Example 1:
NUMBER_OF_ELEMENTS = 5 # For simplicity, use 5 instead of 100
numbers=[] # Create an empty list
sum = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = eval(input("Enter a new number: "))
    numbers.append(value)
    sum += value

average = sum / NUMBER_OF_ELEMENTS
count = 0 # The number of elements above average
for i in range(NUMBER_OF_ELEMENTS):
    if numbers[i] > average:
        count += 1

print("Average is", average)
print("Number of elements above the average is", count)

#Example 2:
list1 = list() # Create an empty list
print()
list2 = list([2, 3, 4]) # Create a list with elements 2, 3, 4
print(list2)
list3 = list(["red", "green", "blue"]) # Create a list with strings
print(list3)
list4 = list(range(3, 6)) # Create a list with elements 3, 4, 5
print(list4)
list5 = list("abcd") # Create a list with characters a, b, c, d
print(list5)

#Example 3:
list1 = [2, 3, 4, 1, 32]
print(len(list1))
print(max(list1))
print(min(list1))
#print(sum(list1))

random.shuffle(list1) # Shuffle the elements in list1
print(list1)


#Example 4:
list1 = [2, 3, 5, 2, 33, 21]
print(list1[-1])
print(list1[-3])

#Example 5:
list1 = [2, 3, 5, 7, 9, 1]
print(list1[2:4])

#Example 6:
list1 = [2, 3, 5, 2, 33, 21]
print(list1[:2])
print(list1[3:])

#Example 7:
list1 = [2, 3, 5, 2, 33, 21]
print(list1[-4 : -2])

#Example 8:
list1 = [2, 3]
list2 = [1, 9]
list3 = list1 + list2
print(list3)

list4 = 3 * list1
print(list4)

#Example 9:
list1 = ["green", "red", "blue"]
list2 = ["red", "blue", "green"]
print(list2 == list1)
print(list2 != list1)
print(list2 >= list1)
print(list2 > list1)
print(list2 < list1)
print(list2 <= list1)

#Example 10:
list1 = [x for x in range(5)] # Returns a list of 0, 1, 2, 3, 4
print(list1)
list2 = [0.5 * x for x in list1]
print(list2)
list3 = [x for x in list2 if x < 1.5]
print(list3)