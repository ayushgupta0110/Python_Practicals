"""
7.Write a menu driven program to perform the following on strings:
a)Find the length of string.
b)Return maximum of three strings.
c)Accept a string and replace all vowels with“#”
d)Find number of words in the given string.
e)Check whether the string is a palindrome or not.
"""

def length_of_string(s):
    print(len(s))


def maximum_of_three_strings(a, b, c):
    print(max(a, b, c))


def Replace(s):
    x = len(s)
    for element in s:
        if element == 'a' or element == 'e' or element == 'o' or element == 'u' or element == 'i':
            s = s.replace(element, '#')

    print(s)


def no_of_words(s):
    count = 1
    for ele in s:
        if ele == " ":
            count = count + 1
    print(count)


def isPalindromic(s):
    k = s[::-1]
    if k == s:
        print("Strings are palindrome")
    else:
        print("Strings are not palindrome")


def main():
    cont = 'y'
    while cont == 'y' or cont == 'Y':
        print("\t\tMENU\n"
              "1. Length of string\n"
              "2. Maximum of three strings\n"
              "3. Replace all vowels with #\n"
              "4. Number of words in a given string\n"
              "5. To check whether string is palindrome or not\n")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            s = input("Enter the string : ")
            length_of_string(s)
        elif choice == 2:
            a = input("Enter the string 1 : ")
            b = input("Enter the string 2 : ")
            c = input("Enter the string 3 : ")
            maximum_of_three_strings(a, b, c)
        elif choice == 3:
            s = input("Enter the string : ")
            Replace(s)
        elif choice == 4:
            s = input("Enter the string : ")
            no_of_words(s)
        elif choice == 5:
            s = input("Enter the string : ")
            isPalindromic(s)
        else:
            print("Invalid choice, choose between (1-5) ")

        print()
        cont = input("Enter y or Y to continue, any other key to exit : ")


if __name__ == '__main__':
    main()
