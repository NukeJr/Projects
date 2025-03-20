import os
folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path,( "mbox-short.txt"))
fhand = open(file_name)

with open(file_name) as fname:
  
  
  many = dict()
  big = 0
  
  
  for line in fhand:
    if line.startswith('From'):
       words = line.split()
       if len(words) > 1:
        email = words[1]
        domain = email.split("@")[-1]
        many[domain] = many.get(domain, 0) + 1

print(many)
            


    