n1 = int(input("Enter list size (NUMERIC List) : "))
l1= []

for i in range(n1) :

    m1 = int(input("Enter no. to append in Numeric List : "))
    l1.append(m1)

n2 = int(input("Enter list size (STRING List) : "))
l2 = []

for i in range(n2) :

    m2 = input("Enter string to append in String List : ")
    l2.append(m2)

l3 = [109, "Shreyan", "Hello", 78, "Python", 95]    #   HYBRID List

#1.    Check if all list elements are Numbers or not

f = 0 
for x in l1 :

    if isinstance(x, int):
      	f += 1

    else :
        f = 0
        break

if f > 0 :
    print(f"all elements in {l1} are Numbers")

elif f == 0 :
    print(f"all elements in {l1} are NOT Numbers")

f = 0 
for x in l2 :

    if isinstance(x, int):
      	f += 1

    else :
        f = 0
        break

if f > 0 :
    print(f"all elements in {l2} are Numbers")

elif f == 0 :
    print(f"all elements in {l2} are NOT Numbers")

f = 0 
for x in l3 :

    if isinstance(x, int):
      	f += 1

    else :
        f = 0
        break

if f > 0 :
    print(f"all elements in {l3} are Numbers")

elif f == 0 :
    print(f"all elements in {l3} are NOT Numbers")

#2.    No. of ODD Values in Numeric List
 
co = 0

for x in l1 :

    if x%2 == 1 :
        co += 1

print(f"No. of odd nos. in {l1} is {co}")

#3.     Largest String

ls = max(l2)

print(f"Largest string in {l2} is {ls}")

#4.     Reverse a list

l11 = l1
l12 = l2
l13 = l3

l11.reverse()
l12.reverse()
l13.reverse()

print(f"Reverse of {l1} is {l11}")
print(f"Reverse of {l2} is {l12}")
print(f"Reverse of {l3} is {l13}")

#5.     Find Specific Element in Lists

k1 = int(input("Enter search element (number) : "))

if k1 in l1 :
    print(f"{k1} is present in {l1}")

else :
    print(f"{k1} is absent in {l1}")

k2 = input("Enter search element (string) : ")

if k2 in l2 :
    print(f"{k2} is present in {l2}")

else :
    print(f"{k2} is absent in {l2}")

k3 = int(input("Enter search element (hybrid) : "))

if k3 in l3 :
    print(f"{k3} is present in {l3}")

else :
    print(f"{k3} is absent in {l3}")

#6.     Find and Remove Specified element

k1 = int(input("Enter search element (number) : "))

if k1 in l1 :
    print(f"{k1} is present in {l1}")
    l1.remove(k1)
    print(f"After removal of {k1}, Updated List is {l1}")

else :
    print(f"{k1} is absent in {l1}") 

#7.     Sorting in DESCENDING Order

l11 = l1

l11.sort()
l11.reverse()

print(f"{l1}, after sorted in DESC. order is {l11}")

l12 = l2

l12.sort()
l12.reverse()

print(f"{l2}, after sorted in DESC. order is {l12}")
'''
l13 = l3

l13.sort()      #   ERROR : Cannot compare 'str' with 'int' and vice-versa
l13.reverse()

print(f"{l3}, after sorted in DESC. order is {l13}")
'''
#8.     Common members

l4 = [1, 2, 3, 4, 7]
l5 = [2, 5, 8, 7]

lc = []

if x in l5 and x in l4 :
    lc.append(x)

print(f"Common elements in {l5} and {l4} are {lc}")