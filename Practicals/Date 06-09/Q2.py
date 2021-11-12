#Ques2. WAP to prompt the user to read an integer between 1 to 7 and display the corresponding day of the
#week.(Use Assertion)

def main():
    day = int(input("Enter number between 1-7:  "))
    assert day>0 and day<=7
    if(day==1):
        print("Monday")
    elif(day==2):
        print("Tuesday")
    elif (day == 3):
        print("Wednesday")
    elif (day == 4):
        print("Thursday")
    elif (day == 5):
        print("Friday")
    elif (day == 6):
        print("Saturday")
    else:
        print("Sunday")

if __name__ == '__main__':
    main()