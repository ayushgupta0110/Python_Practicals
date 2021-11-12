def areaofrect(l,b):
    '''to compute area
    of reactangle using
    length and breadth'''
    area=l*b
    return area
def areaofsq(side):
    '''to compute area
    of square using
    side'''
    areasq=areaofrect(side,side)
    return areasq
def main():
    l=int(input('Enter the length of rectangle: '))
    b=int(input('Enter the breadth of the rectangle: '))
    area=areaofrect(l,b)
    print('area of rectangle: ',area)
    sidesq=int(input('enter side of square'))
    areasq=areaofsq(sidesq)
    print('area of square: ',areasq)
if __name__=='__main__':
    main()
