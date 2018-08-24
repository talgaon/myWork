answer = input("do you want to start game?" "yes or no?")
while answer.lower() != "yes":
    answer = input("do you want to start game?" "yes or no? type yes to start")
if answer.lower() == ("yes"):
    answer2 = input("do you want to go to the beach or the mountain?")
    if answer2.lower() == ("beach"):
        answer3 = input("Do you want to play in the sand or surf?")
        if answer3.lower() == ("sand"):
            print("you built a sand castle")
        elif answer3.lower() == "surf":
            print("you caught a wave")
    elif answer2.lower() == "mountain":
        answer4 = input("Do you want to ski or snowboard?")
        if answer4.lower() == ("ski"):
            print("you lost your ski pole")
        elif answer4.lower() == "snowboard":
            print("you met shaun white")
