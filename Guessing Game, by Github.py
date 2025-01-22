from random import randint

print("Welcome to the Higher-Lower Game!")
rnum = randint(0, 100)
noguesses = 0

while True:
    try:
        guess = input("Guess the number: ")

        if guess.lower() == 'landon':
            print("The secret number is:", rnum)
            print("You found the secret!")
            continue

        if guess.isdigit():
            integer_number = int(guess)
            noguesses += 1
            print("You entered:", integer_number)

            if integer_number > rnum:
                print("My number is Lower")
            elif integer_number < rnum:
                print("My number is Higher")
            else:
                print(f"You win! The number is {guess}! You guessed {noguesses} times.")
                break  # Exit the loop when the user wins
        else:
            print("Invalid input. Please enter an integer number.")

    except Exception as e:
        print("An error occurred:", e)