question1 = input("do you want to start the game?")
while question1.lower() != "yes":
    question1 = input("do you want to start game?")
if question1.lower() == ("yes"):
    word = input("type word for someone to guess.")
    print("\n" * 30)
    Underscore = []
    for i in range(len(word)):
        Underscore.append( "_")

        print  ("your word has", len(word), "letters.")
        guesses = []
        for i in range(5):
            letter = input("guess a letter.", Underscore)
            letter = letter.lower()
            if letter in word:
                print("that is correct")
            else:
                print ("incorect")


                word =[]
                for i in range(len(word)):
                    if word[i] == letter:
                        Underscore[i] = letter
