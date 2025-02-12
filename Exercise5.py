import os 

folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path,("mbox-short.txt"))
file = open(file_name)

count = 0
names = 0

for line in file:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    count += 1
    print(words[2])
print(count,'froms')