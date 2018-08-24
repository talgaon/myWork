for time in range(24):
 if time >= 0 and time <=12:
    print("good morning")
 else:
    if time <=17:
        print("good afternoon")
    elif time <=20:
        print ("good evening")
    if time > 20:
        print ("good night")
