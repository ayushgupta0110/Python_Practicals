import sys

def areaRectangle(length, breadth):
    area = length * breadth;
    return area;

def main():
    if len(sys.argv) == 3:
        lengthRect = int(sys.argv[1])
        breadthRect = int(sys.argv[2])
        areaRect = areaRectangle(lengthRect, breadthRect)
        print('Area of rectangle is', areaRect)
    else:
        print('Unexpected number of command line args')


if __name__ == '__main__':
    main()