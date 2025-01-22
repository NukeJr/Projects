import math
while True:
 try:
   n =  int(input("Write the numeber of sides of your shape: "))
 except:
   print("Invalid Answer")
 Answer = (n - 2) * 180/n
 print("The Interior Angle Measures of you shape is: ",Answer)
 continue
