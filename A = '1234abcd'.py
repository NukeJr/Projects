def show_employee():
   n = "salary:"
   name = input("Write your name: ")
   pay = input("Write your Pay: ")
   if pay == '':
      pay = 9000
      print("Name:" ,name,n,pay)
   print("Name:" ,name,n,pay)
show_employee()