
#
# ages = [5, 12, 3, 56, 25, 78, 1, 15, 41]
#
# sum = 0
# for num in range(len(ages)):
#     sum += ages[num]
# average = sum/len(age)
import json
f = open("json_demo_file.json", "r")
responses = json.load(f)
f.close()

sum = 0
for user in responses:
    age = int(user["age"])
    sum += age
average = sum/len(responses)
print(average)

# dictionary - {"name": "colette", "age":22 }
# age_value = dictionary["age"]

# alist = [0,2 ]
# seceond_value = alist[1]
