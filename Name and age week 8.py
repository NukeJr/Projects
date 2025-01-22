# Name and Age Practice
def yello(name, age):
    print("Hello,", name)
    print("Your age is,", age)

# Biggest Number Output Practice
def order(a, b, c):
    big = max(a, b, c)
    print("The biggest of your numbers is:", big)

# Print All Values Practice
def n(q, w, e):
    print("Printed Values:")
    print(q)
    print(w)
    print(e)

# Adding Numbers
def answer(f, g, h, i, j, k, l):
    pl = f + g + h + i + j + k + l
    print("The sum is:", pl)

# Multiplying Numbers

def answerd(fd, gd, hd, id, jd, kd, ld):
    pd = fd * gd * hd * id * jd * kd * ld
    print("The sum is:", pd)


# Name and Age
name = input("Hello, what is your name?: ")
age = input("What is your age?: ")
try: 
    age = int(age)
    yello(name, age)
except ValueError:
    print("Invalid Answer: Age must be a number.")

# Biggest Number
a = input("Please type a whole number: ")
b = input("Please type a whole number: ")
c = input("Please type a whole number: ")
try:
    a, b, c = int(a), int(b), int(c)
    order(a, b, c)
except ValueError:
    print("Invalid Answer: Please enter whole numbers.")

# Print Values
q = input("Write a word or number: ")
w = input("Write a word or number: ")
e = input("Write a word or number: ")
n(q, w, e)

# Adding Numbers
try:
    f = int(input("Write a whole number: "))
    g = int(input("Write a whole number: "))
    h = int(input("Write a whole number: "))
    i = int(input("Write a whole number: "))
    j = int(input("Write a whole number: "))
    k = int(input("Write a whole number: "))
    l = int(input("Write a whole number: "))
    answer(f, g, h, i, j, k, l)
except:
    print("Invalid Answer: Please enter whole numbers.")

# Multiplying Numbers
try:
    fd = int(input("Write a whole number: "))
    gd = int(input("Write a whole number: "))
    hd = int(input("Write a whole number: "))
    id = int(input("Write a whole number: "))
    jd = int(input("Write a whole number: "))
    kd = int(input("Write a whole number: "))
    ld = int(input("Write a whole number: "))
    answerd(fd, gd, hd, id, jd, kd, ld)
except:
    print("Invalid Answer: Please enter whole numbers.")

# Subtrating and Multiplying

res = caculations(add)

