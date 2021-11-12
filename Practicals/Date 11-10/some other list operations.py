#   String Splitting

items = "Jane John Peter Susan".split()
print(items)

items = "09/20/2012".split("/")
print(items)

#   Inputting Lists

l = []

print("Enter 10 nos. in to the list :")

for i in range(10) :
    m = int(input("Enter no. to append the list : "))
    l.append(m)

print(l)

# Read numbers as a string from the console

s = input("Enter 10 numbers separated by spaces from one line: ")
items = s.split() # Extract items from the string
lst = [eval(x) for x in items] # Convert items to numbers