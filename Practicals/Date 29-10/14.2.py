set1={"green","red","blue"}
print(set1)
set2=set([4,7,8,1,2,9])
print(set2)
print("Is red in set1?","red" in set1)
print("Length of set2: ",len(set2))
print("max of set2: ",max(set2))
print("min of set2: ",min(set2))
print("sum of set2: ",sum(set2))
set3=set1 | {"green","yellow"}
print(set3)
set3=set1 - {"green","yellow"}
print(set3)
set3=set1 & {"green","yellow"}
print(set3)
set3=set1 ^ {"green","yellow"}
print(set3)
list1=list(set2)
print(set1=={"green","red","blue"})
set1.add("yellow")
print(set1)
set1.remove("yellow")
print(set1)
