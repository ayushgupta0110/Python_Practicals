# 10. Write a function that takes a sentence as input from the user and calculates
# the frequency of each letter. Use a variable of dictionary type to maintain the count.

def main():
    sen = input("Enter a sentence : ")
    freq = {}

    for i in sen:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print(f"Count of all characters in {sen} is : {str(freq)}")


if __name__ == '__main__':
    main()