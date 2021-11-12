

def authenticateUser(passsword):
    if passsword == "magic":
        message = "Login successful!! \nWelcome to the system"
    else:
        message = "Password mismatch!!\n"
    return message


def main():
    print(" \t Login System")
    password = input("\nPlease enter password: ")
    message = authenticateUser(password)
    print(message)

if __name__ == '__main__':
    main()

