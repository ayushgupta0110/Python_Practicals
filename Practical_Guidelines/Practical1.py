"""
1 . Write a function that takes the lengths of three sides: side1 , side2 and side3 of
the triangle as the input from the user using input function and return the area
and perimeter of the triangle as a tuple. Also, assert that sum of the length of any
two sides is greater than the third side
"""
import math


def getAP(s1, s2, s3):
    perimeter = (s1 + s2 + s3)
    s = perimeter / 2
    area = math.sqrt((s * (s - s1)*(s - s2)*(s - s3)))
    APTuple = (area, perimeter)
    return APTuple


def main():
    s1 = eval(input("Enter side1: "))
    s2 = eval(input("Enter side2: "))
    s3 = eval(input("Enter side3: "))
    assert s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1, "This is not a valid triangle"
    my_tuple = getAP(s1, s2, s3)
    print("Area is: ", my_tuple[0])
    print("Perimeter is : ", my_tuple[1])


if __name__ == '__main__':
    main()
