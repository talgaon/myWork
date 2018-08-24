# --- Define your functions below! ---
# --- Put your main program below! ---
def




def goodbye():
    print("see ya")

def greetings(input):
    print("Hey")

def say_default():
    print("thats cool")

def is_valid_input(user_input, valid_responses):
    return answer in greeting

def process_input(answer):
    greetings = ["hey", "hi", "hello" "hola", "heyo", ]
    goodbyes =["bye", "goodbye"]
    if is_valid_input(answer, greetings):
        greetings()
    elif is_valid_input(user_answer, goodbyes):
        goodbye()

    else:
        say_default()


def main():
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
