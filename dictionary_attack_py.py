#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
def checkNum():


def removeSubstitutes(password):
    dict = {"4":"a", "0":"o", "5":"s", "1":"l", "3":"e"}

def checkDictionary(password, words):

    if test_password in words:
        print("your password is not secure")
    else:
        print ("good password")

def main():
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
    test_password = test_password.replace(test_password)



if __name__ == '__main__':
    main()
