from random import*
Main= ["chicken",  "steak",  "pasta",  ]

sideDish = [" fish",  " bread",  " buttered bread",  " salted bread"]

Drink = [" Water",  " wine",  " vodak",  " sprite"]
for i in range(5):
    randomfood = randint(0,len(Main)-1)
    randomfood2 = randint(0,len(sideDish)-1)
    randomfood3 = randint(0,len(Drink)-1)

    print(Main[randomfood] + sideDish[randomfood2] + Drink[randomfood3])
