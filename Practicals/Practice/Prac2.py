def areaRectangle(length, breadth):
    '''
    Objective: To compute area of rectangle
    Input Parameters: length, breadth - numeric value
    Return value: area - numeric value
    '''    
    area = length * breadth
    return area

def areaSquare (side):
    '''
    Objective: To compute area of square
    Input Parameter: side - numeric value
    Return value: area - numeric value
    '''    
    area = areaRectangle (side, side)
    return area

def main():
    '''
    Objective: To compute area of rectangle and square based on
    user input
    Input Parameter: None
    Return value: None
    '''
    print("Enter the following values for rectangle:'")
    len = int(input('Length : integer value: '))
    br = int(input('Breadth : integer value: '))
    areaRect = areaRectangle(len,br)
    print('Area of rectangle is', areaRect)
    sideSqr = int(input('Enter side of square: integer value: '))
    areaSqr = areaSquare(sideSqr)
    print('Area of square is', areaSqr)

if __name__ == '__main__':
    main()  