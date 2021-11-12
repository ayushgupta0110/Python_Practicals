NUMBER_OF_ELEMENTS = 5
numbers =[]
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

########################################

list1 = []          # Same as list()
list2 = [2, 3, 4]   # Same as list([2, 3, 4])
list3 = ["red", "green"]    # Same as list(["red", "green"])
list4 = list("abcd")        # Create a list with characters a, b, c, d

print(list1)
print(list2)
print(list3)
print(list4)

#########################################

list1 = ["green", "red", "blue"]
list2 = ["red", "blue", "green"]
print(list2 == list1)
print(list1!=list2)
print(list1>list2)
print(list1<list2)
max(list1)
min(list1)