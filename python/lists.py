from random import*
firstnames = ["Alexander", "Aaron", "Maria", "Angelica"]

lastnames = [" Hamilton", " Burr", " Rhynolds", " schyler"]
for i in range(10):
    randomName = randint(0,len(firstnames)-1)
    randomName2 = randint(0,len(lastnames)-1)
print(firstnames[randomName] + lastnames[randomName2])
