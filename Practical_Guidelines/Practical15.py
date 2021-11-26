"""
15. Define a class Student to store his/ her name and marks in three subjects.
    Use a class variable to store the maximum average marks of the class.
    Use constructor and destructor to initialize and destroy the objects.
"""


class Student:
    max_average = 0

    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, marks):
        self.marks.append(marks)

    def get_average(self):
        return sum(self.marks) / len(self.marks)

    def __del__(self):
        print("Student object destroyed")


def main():
    student1 = Student("John")
    student1.add_marks(90)
    student1.add_marks(80)
    student1.add_marks(70)
    print(student1.get_average())
    student2 = Student("Mary")
    student2.add_marks(95)
    student2.add_marks(85)
    student2.add_marks(75)
    print(student2.get_average())
    if student2.get_average() > student1.get_average():
        print("Mary's average is higher")
        Student.max_average = student2.get_average()
    else:
        print("John's average is higher")
        Student.max_average = student1.get_average()

    print("The maximum average marks is: " + str(Student.max_average))


if __name__ == '__main__':
    main()
