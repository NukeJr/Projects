import os 

folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path,input( "File name: "))
file = open(file_name)
#print(file.read())

print(folder_path)

romeo = file

jk = []

lists = file

for line in lists:
    line = line.rstrip()
    for word in line.split():
       if word not in jk:
          jk.append(word)
jk.sort()
print (jk)

