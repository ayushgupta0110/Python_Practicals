#   Addition and Mutation

students = {"20512": "Ayush", "20513": "Chinmay", "20520": "Amit", "20549": "Siddhant", "20550": "Smaran"}

print(students.keys())
print(students.items())

print(students["20512"])

print()

students["20512"] = "Ayush Gupta"  # Mutate key no. 20512

print(students.keys())
print(students.items())

print(students["20512"])  # Ayush Gupta

print()

#   Looping

for key in students:
    print(f"{key} : {students[key]}")

print()

#   Deletion

del students["20512"]

for key in students:
    print(f"{key} : {students[key]}")

#   Test of Presence of Keys in Dict.

print()

print("20549" in students)  # TRUE
print("20546" in students)  # FALSE

#   Other ops.

students["20551"] = "Aman"
students["20553"] = "Akash"
students["20543"] = "Ashu"
students["20541"] = "Ankur"

print()

print(students.keys())
print(students.values())
print(students.items())

print(students.get("20512"))  # Ayush Gupta

print(students.pop("20513"))  # RETURN n POP Chinmay

print(students.popitem())  # RETURN n POP random item

students.clear()  # All entries CLEARED
print(students.items())
