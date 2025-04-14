# Exercise 1: Basic Class Definition
class Animal(object):
    def __init__(self, name, Makesound):
        self.makesound = Makesound
        self.name = name 
# Define a basic class called Animal with a method called make_sound that prints a sound.
    def Makesound(self):
        print('Moooo!')
    def print_name(self):
        print(f"Hello, My name is",self.name,".")
    

# Create an instance of Animal and call the make_sound method.
Cow = Animal('Momo','Moooo')
Cow.Makesound()
Cow.print_name()



# Exercise 2: Inheritance
class Dog(Animal):
    def  __init__(self, name, Makesound):
        super().__init__(name, Makesound)

# Create a subclass of Animal called Dog that overrides the make_sound method
    def Makesound(self):
        print('Bark!')
    def print_name(self):
        print(f"Hello, My name is",self.name,".")
# Create an instance of Dog and call the make_sound method.
Doggy = Dog("Bill","Barky")
Doggy.Makesound()
Doggy.print_name()
# Exercise 3: Adding Attributes
# Add an attribute to the Animal class and initialize it through the constructor.

# Update the Dog class to use the new attribute and update the make_sound method to use the attribute.

# Create an instance of Dog with a name and call the make_sound method.


class Cat(Animal):
    def  __init__(self, name, Makesound):
        super().__init__(name, Makesound)

# Create a subclass of Animal called Dog that overrides the make_sound method
    def Makesound(self):
        print('Meow!')
    def print_name(self):
        print(f"Hello, My name is",self.name,".")
# Create an instance of Dog and call the make_sound method.
Kitty = Cat("Daisy","Meow")
Kitty.Makesound()
Kitty.print_name()



# Exercise 4: Multiple Subclasses
# Create another subclass of Animal called Cat that also overrides the make_sound method.

# Create instances of Dog and Cat and call their make_sound methods.