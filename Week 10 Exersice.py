largest = None
smallest = None

while True:
    user_input = input("Enter a number(or 'done' if finished)")

    
    if user_input.lower() == 'done':
        break

    try:
        num = int(user_input)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError: 
        print("Invalid input, please enter a valid number.") 
    if largest is not None and smallest is not None:
        print(f"Largest number: {largest}")
        print(f"Smallest number: {smallest}")
    else:
        print("No valid numbers were entered.")