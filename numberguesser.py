from random import seed
from random import randint
import time

seed(time.time())

Greeting = "Hello there! This is a just a simple guessing game to see if you can guess my random number between 1 and 10."

myNumber = randint(1, 10)       
print(myNumber)


solved = False

while solved != True:
    try:
        guessed = int(input("Take a guess!"))

    except ValueError:
        print ("Not an integer! Try again!")
        continue

    myguess = guessed
    int(myguess)

    if myguess < myNumber:
        print("Higher!")
    elif myguess > myNumber:
        print("Lower!")
    else:
        print("You nailed it")
        solved = True