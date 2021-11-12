def reverse(n):
    rev = 0
    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev

def isPalindrome(num):
    rev= reverse(num)
    if num == rev:
        return True
    else:
        return False

def main():
    num = int(input("Enter the number: "))
    if isPalindrome(num):
        print(num," is a Palindrome")
    else:
        print(num," not a Palindrome")

if __name__ == '__main__':
    main()
