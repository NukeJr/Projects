import random 
import math

Landon = random.randint(0, 1005)
input = input("Pick any whole number less than 1,000:",)

if int(Landon) > int(input) == True:
  print ("My number is bigger than",input)
  print("My number is:",Landon)

if int(Landon) > int(input) == False:
   print("Your number is higher!")
   print("My number is:",Landon)