import random

print("In this game, you are going to try to roll a higher roll than mine.")

while True:
    try:
        # Get the number of sides for the dice
        dr = int(input("How many sides does your dice have: "))
        
        # Check if the number of sides is valid
        if 6 <= dr <= 100:  # Adjusted the range to be between 6 and 100
            break  # Valid input, exit the loop
        else:
            print("Try a different dice side number. (Can't be a negative, a decimal, fraction, higher than 100, or less than 6)")
    except ValueError:
        print("That's not a valid number. Please enter a whole number.")

# Rolling the dice (from 1 to dr)
mroll = random.randint(1, dr)
yroll = random.randint(1, dr)

# Determine the result
if mroll > yroll:
    print("Sorry, I win! Your roll was:", yroll)
    print("My roll is:", mroll)
elif mroll < yroll:
    print("You win! Your roll was:", yroll)
    print("My roll is:", mroll)
else:
    print("It's a tie! Yours and my roll was:", yroll)