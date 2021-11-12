import os.path
import sys


def main():
    keyWords = {"and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}

    fileName = input("Enter a Python source code filename: ").strip()  # Enter a File Name

    if not os.path.isfile(fileName):  # Check for Desired File
        print(f"File {fileName} does not exist")
        sys.exit()

    infile = open(fileName, "r")  # Opens File for INPUT (READ)

    text = infile.read().split()  # Read and split words from the file

    count = 0

    for word in text:

        if word in keyWords:
            count += 1

    print("The number of keywords in", fileName, "is", count)


main()
