l1 = [1, 2]
l2 = [3, 4, 5]

print(f"ID of List 1 = {l1} is {id(l1)}")
print(f"ID of List 2 = {l2} is {id(l2)}")

l2 = l1
print(f"ID of List 2 after copying is {id(l2)}")

if id(l2) == id(l1) :
    print("which is same as that of List 1 initially")

else :
    print("which is NOT same as that of List 1 initially")