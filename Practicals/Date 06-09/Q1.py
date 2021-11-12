
#Ques1. WAP to read an integer and check whether the number is positive , negative or zero. Print the result


def main():
    num = int(input("Enter the number: "))
    if(num>0):
        print(num , " is Positive")
    elif(num<0):
        print(num , " is negative")
    else:
        print(num , " is zero")

if __name__ == '__main__':
    main()