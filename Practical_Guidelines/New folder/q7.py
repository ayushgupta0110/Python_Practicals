def length_of_string(s):

    print(len(s))

def max_of_three_strings(a,b,c):

    print(max(a,b,c))

def ReplaceVow(s):

    x = len(s)

    for elements in s:

        if elements == 'a' or elements == 'e' or elements == 'o' or elements == 'u' or elements == 'i' or elements == 'A' or elements == 'E' or elements == 'O' or elements == 'U' or elements == 'I':
          s = s.replace(elements,'#')

    print(s)
'''
def no_of_words(s):

    s.strip()   #   Removes all LEADING and TRAILING white-spaces, if any

    count = 0

    for elements in s:

        if elements == " ":
            count += 1

    print(count + 1)
'''
def no_of_words(s):

    res = s.split()     #   Creates a LIST with all words separated
    c = 0
    
    for x in res : 
        c += 1

    print(res)

def isPalin(s):

    k = s[::-1]

    if k == s:
        print("Strings are palindromic")

    else:
        print("Strings are not palindromic")

def main():

    ok = 1

    while(ok == 1):
        print("MENU\n"
        "1. Length of string\n"
        "2. Maximum of three strings\n"
        "3. Replace all vovels with #\n"
        "4. Number of words in a given string\n"
        "5. To check whether string is palindromic or not\n")

        num = int(input("Choose one option from menu : "))

        if num == 1:
            s = input("Enter the string : ")
            length_of_string(s)

        elif num == 2:
            a = input("Enter the string a : ")
            b = input("Enter the string b : ")
            c = input("Enter the string c : ")
            max_of_three_strings(a,b,c)

        elif num == 3:
            s = input("Enter the string : ")
            ReplaceVow(s)

        elif num == 4:
            s = input("Enter the string : ")
            no_of_words(s)

        elif num == 5:
            s = input("Enter the string : ")
            isPalin(s)

        print()

        cont = int(input("Enter 1 to CONTINUE or any other number to EXIT : "))
        ok = cont

main()