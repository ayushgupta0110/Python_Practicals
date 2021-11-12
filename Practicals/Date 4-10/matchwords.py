def nmatchchars(str1, str2):
    '''
    To count the no. of distinct matching characters in the str1 and str2
    input - str1,str2 - string
    return count - int
    '''

    count=0
    for i in range(len(str1)):
        ch = str1[i]
        if ch not in str1[:i]:
            for char in str2:
                if char == ch:
                    count = count + 1
                    break
    return count

def main():
    str1 = input('Enter string 1: ')
    str2 = input('Enter string 2: ')
    count = nmatchchars(str1,str2)
    print("Number of distinct common characters: ", count)

if __name__ == '__main__':
    main()



