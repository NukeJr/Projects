import random
def Y(): 
    return "Your number was:"
def M():
    return "And my number was:"
while True:
    Name = input ("What's your name? ")
    print("Hello,",Name)
    print("So,",Name,"what would you like to do? 1: play a game or 2: go to bed")

    Path = input("Write either 1 or 2: ")


    if Path not in {'1', '2'}:
        print("Try a different answer")
        continue
    else:
     if Path == '2':
        Bed = input("Good night! Enter 1 when awake: ")
        
    
    if Path == '1' or (Path == '2' and Bed == '1'):
        print("This is a guessing game! You are I are going to pick a number from 1 to 10, and if you pick my number, you win!")

        Guess = int(input("Pick a number from 1-10:"))
        mn = random.randint(1, 10)

        if mn < Guess:
            print("You guessed higher!", Y(),Guess)
            print(M(),mn)
        elif mn > Guess:
            print("You guessed lower!",Y(),Guess)
            print(M(),mn)
        else:
            print("You guessed it!",Y(),Guess)
            print(M(),mn)
          
        yay = input("Thanks for playing! Do you want to play agian? If so type 3")
        if yay == '3':
            continue
        else:
            break
        
