# Program to Create a Class and Get All Possible Subsets from a Set of Distinct Integers

class sub:
    def __init__(self):
        pass

    def f1(self, s1):
        return self.f2([], sorted(s1))

    def f2(self, curr, s1):
        if s1:
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
        return [curr]


def main():
    a = []
    n = int(input("Enter number of elements of list: "))
    for i in range(0, n):
        b = int(input("Enter element: "))
        a.append(b)
    print("Subsets: ")
    print(sub().f1(a))


if __name__ == '__main__':
    main()