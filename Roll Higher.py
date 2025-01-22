import math
import random

print("In this game you are going to try to roll a higher roll than mine.")
while True:
   try:
     dr = int(input("How many sides does your dice have:" ))     
     if 6 <= dr <= 100:
          break
     else:
         print("Try a different dice side number.(Can't be a negative, a decimal, fraction, higher than 100 or less than 6)")
   except ValueError:
       print("That's not a valid number. Please enter a whole number.")
    
mroll = random.randint(1, dr)
yroll = random.randint(1, dr)
if (mroll > yroll):
     print("Sorry I Win, your roll was:",yroll)
     print ("My roll is:",mroll)
elif (mroll < yroll): 
      print("You Win!, your roll was:",yroll)
      print ("My roll is:",mroll)
else: 
      if  (mroll==yroll):
         print ("It's a tie! Yours and my roll was:",yroll)