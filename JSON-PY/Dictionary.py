 # questions = {"what is your name?", "how old are you?","what is your birthday?"}
import json




while True:
     question = input("what is your name ")
     second_question = input("what is your age")
     third_question = input("when is your birthday ")

     (question+second_question+third_question)
     start_again = input("do you want start again")
     if start_again == "yes":
         continue
     else:
         break


f = open("jsonPython.json", "r")
json.loads(question)


f.close()



f = open("jsonPython.json", "w")
json.dump(question , f)


f.close()


# names_age = {
# 'eden':28,
# 'gilad':26,
# 'ehud':23,
# 'clara':21
# }

#for key, value in names_age.items():
    #print(key, ":", value)


# name = input("what is your name?")
# age = input("How old are you?")
# habbit = input("what is a weird habbit you have?")
# birthday = input("what is your birthday?")




#
# def question():
#      responses = {}
#      questions = ["what is your name?", "how old are you?","what is your birthday?"]
#      return responses
#
#
#  def main():
#      responses = []
#
#
#      responses.append(responses()):
#
#  if __name__ == '__main__':
#      main()


# responses = {}
# keys = ["name", "age","birthday"]
# for i in range(len(questions)):
#     responses[keys[i]] = input(questions[i])

# survay = {}
# survay['age'] = age
# survay['name']= name
# survay['habbit']=habbit
# survay['birthday']=birthday

#
# for key, value in responses.items():
#     print(key, ":", value)
