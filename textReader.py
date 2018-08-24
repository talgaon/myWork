import json

zipCode = open("zipcode.txt", "r")
coordinates = []
for line in zipCode:
    line.strip()
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    line = line.split(",")
    coordinates.append(line)
with open("visionary.json", "w") as f:
    json.dump(coordinates, f)
