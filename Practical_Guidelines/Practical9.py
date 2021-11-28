"""
9.  Use dictionary to store marks of the students in 4 subjects. Write a function to
    find the name of the student securing highest percentage.
    (Hint: Names of students are unique).
"""

def maxPer(stud, per):
    mp = max(per)
    c = 0
    for i in per:
        if i == mp:
            print(f"Max. percentage is {mp} which is obtained by {stud[c]}")
        else:
            c += 1


def main():
    n = int(input("Enter no. of students: "))
    lstud = []
    lsub = []
    lper = []

    print("\nEnter names of students' : ")
    for i in range(n):
        m = input(f"Enter Student {i + 1} name : ")
        lstud.append(m)

    print("\nEnter subject names(min-4) : ")
    for i in range(4):
        m = input(f"Enter Subject {i + 1} name : ")
        lsub.append(m)


    for j in lstud:
        sum = 0
        per = 0
        lmarks = []

        print()
        print(f"Entries for {j} : ")

        for i in range(4):
            m = int(input(f"Enter marks obtained in {lsub[i]} : "))
            lmarks.append(m)
            sum += m

        print()
        print(f"Marks Details of {j} : {dict(zip(lsub, lmarks))}")

        per = (sum / 400) * 100
        lper.append(per)

    maxPer(lstud, lper)  # MAX. PERCENTAGE func.


if __name__ == '__main__':
    main()