#! python3
#Guessing Game Challenge
#Authoer: Josh Smith

import random

def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
     the user,until a valid `int` is entered.

    :param prompt: The String that the user will see
        when they're prompted to enter the value.
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not a valid number".format(temp))


print("\nWelcome to Josh's Guessing Game! This game is customizable. "
      "\nYou may choose the highest number and your number of tries. "
      "\nI suggest 10 tries with a highest number of 1000. "
      "\nPress any key to get started.")
input("")

highest = get_integer("\nPlease enter the highest number "
                            "(I suggest 1000):")

leftCount = get_integer("\nPlease enter the number of tries "
                              "(I suggest 10):")

answer = random.randint(1, highest)
tryCount = 0
tries = leftCount
while tryCount != tries:
    guess = get_integer("\nPlease guess a number between 1 and {0}."
                              " You have {1} attempts left. ("
                              "Select 0 to quit):"
                              .format(highest, leftCount))
    if guess == answer:
        print("\nYou guessed the correct number {}. Congrats!"
              .format(answer))
        print("Number of  incorrect tries: {}"
              .format(tryCount))
        break
    elif guess < answer and guess != 0:
        print("\nToo low. Try again.")
        tryCount += 1
        leftCount -= 1
        print("Number of tries: {}".format(tryCount))
    elif guess > answer:
        print("\nToo High. Try again.")
        tryCount += 1
        leftCount -= 1
        print("Number of tries: {}".format(tryCount))
    elif guess == 0:
        break
if tryCount == tries:
    print("\nYou've exhausted all attempts.\nThe number was {}"
          .format(answer))
print("\nGame Over")
over = input()

