print("Welcome to Quiz 1!")
Student_name = input("Please enter your name: ")

print("Quiz 1 will now begin", Student_name)

score = 0


answer = input("What does the 'print()' function do? ")
if answer == "Prints a message on the screen":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


answer = input("What does the 'input()' function do? ")
if answer == "Allows the user to input a value":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does the 'if' statement do? ")
if answer == "Allows the user to make a choice":
    print("Correct!")
    score += 0.5
else:
    print("Incorrect")

answer = "What does the 'else' statement do? "
if answer == "Provides an alternative to the 'if' statement":
    print("Correct!")
    score += 0.5
else:
    print("Incorrect")


    print("The quiz is now over\n Congradulations!Your score is", score)
