import random

Name = input ("What's your name? ")
print("Hello,",Name)
print("So,",Name,"what would you like to do? 1: play a game or 2: go to bed")
Path = input("Write either 1 or 2: ")

if Path not in {'1', '2'}:
    print("Try a different answer")
else:
    if Path == '2':
        Bed = input("Good night! Enter 1 when awake: ")
    
    if Path == '1' or (Path == '2' and Bed == '1'):
        print("This is a guessing game! You are I are going to pick a number from 1 to 10, and if you pick my number, you win!")

        Guess = int(input("Pick a number from 1-10:"))
        mn = random.randint(1, 10)

        if mn < Guess:
            print("You guessed higher! Your number was:",Guess)
            print("And my number was:",mn)
        elif mn > Guess:
            print("You guessed lower! Your number was:",Guess)
            print("And my number was:",mn)
        else:
            print("You guessed it! Your number was:",Guess)
            print("And my number was:",mn)

        print ("Thanks for playing! Click the triangle in the top right cornerro play again.")