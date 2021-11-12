def main():
    keyWords = {"and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}

    text = ("and", "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "del", "assert", "import")
    count = 0
    for word in text:
        if word in keyWords:
            count += 1

    print("The number of keywords in text is", count)


if __name__ == '__main__':
    main()
