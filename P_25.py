import re

# This function makes sure the user gives a valid name:
def validate_name(name):
   return bool(re.match(r"^[A-Za-z]+( [A-Za-z]+)?$", name))
# Using the validate_name function
name = validate_name(input("New contact's name: "))
print(name)

# This function makes sure the user gives a valid phone number:
def validate_phone(number):
   return bool(re.match(r"^\d{3}-?\d{3}-?\d{4}$", number))
# Using the validate_phone function
number = validate_phone(input("New contact's phone number: "))
print(number)

