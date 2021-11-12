
def main():
    number = eval(input('Input a number: '))
    if number%2==0 or number%3==0:
        print('number is divisible either by 2 or 3')
    else:
        print('number divisible neither by 2 nor by 3')
    if number%2==0 and number%3==0:
        print('number is divisible by both 2 and 3')
    else:
        print('number not divisible by 2 and 3')
    if number%2==0 or number%3==0 and not number%2==0 and number%3==0:
        print('number is divisible either by 2 or 3 but not by both')

if __name__== '__main__':
    main()