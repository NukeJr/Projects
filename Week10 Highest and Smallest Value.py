Highest_number = None
Smallest_number = None
countdown = 5
for value in {23 ,25 ,36 ,35 ,36 ,123 ,2 ,67}:
      if Smallest_number == None:
        Smallest_number = value
      if Highest_number == None:
        Highest_number = value
      if Highest_number < value:
        Highest_number = value
      if Smallest_number > value:
        Smallest_number = value
print("The smallest number is:",Smallest_number)
print("The biggest number is:",Highest_number)