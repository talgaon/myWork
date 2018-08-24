

def removeSubstitutes(password):
    substitutions = {
        "1": "l",
        "!": "i",
        "2": "z",
        "3": "e",
        "@": "a",
        "4": "a",
        "$": "s",
        "5": "s",
        "6": "g",
        "7": "t",
        "8": "b",
        "9": "g",
        "0": "o"
    }
    # for each character in password
    for i in password:
        # check if it's a key in my substitute dictionary
        if i in substitutions:
            # replace substitute for original letter
            password = password.replace(i, substitutions[i])
    return password

def removeNumTail(password):
    for i in range(len(password)):
        if password[i].isnumeric():
            if password[i:].isnumeric():
                return password[:i]
    return password

def twoWords(password, words):
    for i in range(len(password)):
        if password[:i]in words and password[i:] in words:
            return True
    return False

def checkDictionary(password, words):
    if password in words:
        print ("Your password is not secure!")
    else:
        print ("Good password")


    # for test_password.index()
    #         # check if it's a key in my substitute dictionary
    #     if test_password.isdigit()
    #             # replace substitute for original letter
    #         password = password.split([i])
    # print(password)

def main():
    #Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
    f = open("dictionary.txt","r")

    print("Can your password survive a dictionary attack?")

    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password: ")

    #Write logic to see if the password is in the dictionary file below here:
    words = []
    for line in f:
        line = line.strip()
        words.append(line)
    f.close()

    test_password = removeNumTail(test_password)
    if twoWords(test_password, words):
        print ("Your password is not secure!")
    else:
        print ("Good password")
    # test_password = numbers(test_password)
    # checkNum(test_password, words)

    checkDictionary(test_password, words)

if __name__ == '__main__':
    main()
