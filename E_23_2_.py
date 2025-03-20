import os
folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path,( "mbox-short.txt"))
fhand = open(file_name)

times = []

with open(file_name) as fname:  
  for line in fhand:
    if line.startswith('From'):
       words = line.split()
       if len(words) > 5:
         time = words[5]
         times.append(time)
times.sort()
print(times)
            


