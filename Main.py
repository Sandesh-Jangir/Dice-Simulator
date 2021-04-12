import random

# Greeting User
print("Welcome To Dice Simulator \nLeave Blank For Next Turn or Write 'exit' To leave")

# Mainloop
while True:
    Command = input(": ")

    if Command=="":
        Number = random.randint(1 , 6)
        print("It's", Number)

    elif Command == "exit":
        print("Thanks For Using Dice Simulator")
        break

    else:
        print("Invalid Value")