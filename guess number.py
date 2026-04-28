import random

print("WELCOME TO THE 'GUESS THE NUMBER GAME'")
name = input("enter the username:")

again = "y"

while again.lower() == "y":

    print("choose the difficulty level:")
    difficulty = int(input("TYPE '1' for EASY [5 lives] / TYPE '2' for HARD [2 lives]:"))
    if difficulty == 1:
        attempt = 5
        number = random.randint(1,30)
        print("you chose EASY")
        print("GUESS THE NUMBER BETWEEN 1 - 30")
    elif difficulty == 2:
        attempt = 2
        number = random.randint(1,67)
        print("you chose HARD")
        print("GUESS THE NUMBER BETWEEN 1 - 67")
    else:
        print("Invaild choice default to EAST")
        attempt = 5
        number = random.randint(1,30)
        print("GUESS THE NUMBER BETWEEN 1 - 30")


    guessed = False
    
    
    for i in range(attempt):
        guess = int(input("enter the guess:"))
        if guess < number:
            print("Too LOW!")
        elif guess > number:
            print("Too HIGH!")
        else:
            print("CORRECT GUESS!",name)
            guessed = True
            break

    if guessed == False:
        print("YOU LOSE!",name,"Number was:",number)
    
    again = input("PLAY AGAIN!(y/n):")
    
