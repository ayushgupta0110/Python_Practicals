# Program to Create a Class in which One Method Accepts a String from the User
# and Another Prints it

class Info:
    def __init__(self):
        self.name = input("Enter name: ")

    def display(self):
        print(f"Name entered is {self.name}")


def main():
    while True:
        c1 = Info()
        c1.display()
        ch = input("To continue press y, any other key to exit: ")
        if ch != 'y':
            break


if __name__ == '__main__':
    main()