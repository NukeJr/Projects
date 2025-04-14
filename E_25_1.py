

# Exercise 1: Create a class called `Person` that has the following attributes:
class Person(object):
    def __init__(self, name, age, email, intro):
        self.name = name
        self.age = age
        self.email = email
        self.intro = intro
    def print_name(self):
        print("Name is",self.name)
    def print_age(self):
        print("Age is:",self.age)
    def print_email(self):
        print("Email is:",self.email)
    def print_intro(self):
        print('Hello, my name is',self.name,'I am',self.age,'years old! My email is:',self.email)

Prsn = Person('Tim',5,'Tim@gmail.com','')
Prsn.print_name()
Prsn.print_age()
Prsn.print_email()
Prsn.print_intro()
# - name (string)
# - age (integer) 
# - email (string)
# The class should have a method called `introduce` that prints a message introducing the person.



# Exercise 2: Create a class called `Book` that has the following attributes:
class Book(object):
   def __init__(self,title,author,pages,summary):
       self.author = author
       self.pages = pages
       self.title = title  
       self.summary = summary 
# - title (string)
   def print_title(self):
       print('The title of my book is:',self.title)
# - author (string)
   def print_author(self):
       print('My name is:',self.author,'and I am the author.')
# - pages (integer)
   def print_pages(self):
       print('The number of pages:',self.pages)
# The class should have a method called `summary` that prints a summary of the book.
   def print_summary(self):
       ('Jason is working at the zoo when suddenly the hippo seems to be singing and then leaning closer Jason falls into the world of the Beyonders. Read this fantactic tale by:',self.author,'the page number is:',self.pages,'and is called:',self.title)
BK = Book('Beyonders','Brandon Mull',378,'')
BK.print_author()
BK.print_pages()
BK.print_summary()
BK.print_title()



# Exercise 3: Create a class called `Library` that has the following attributes:
class Library(object):
    def __init__(self,name,books,members,add):
        self.name = name
        self.books = books
        self.members = members
        self.add = add
    def print_name(self):
        print('Hello I am the librarian. My name is:',self.name)
    def print_books(self):
        print('We have a bunch of books, but here is our favorites',self.books)
    def print_members(self):
        print('Here is some of our crew:',self.members)
    def print_add(self):
        print()
pr = Library('Bob','Beyonders, Candyshop War, Harry Potter, 5 Kingdoms, The Penderwicks.','Shauna, Terry, Franco, Bill, Joe','')
pr.print_name()
pr.print_books()
pr.print_members()
pr.print_add()
# - name (string)
# - books (list of Book objects)
# - members (list of Person objects)
# The class should have methods to add a book, add a member, and display the library's information.


# Exercise 4: Create an objects of the Person, Book, and Library classes and test their methods: