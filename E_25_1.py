import re
import os

folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path, "mbox-short.txt")

with open(file_name) as fhand:
 file = 0
 stuff = input("Enter a regular expression: ")
 for i in fhand:
     print(i)
     i.strip()
     print(i)
     try:
        print('worked')
        p = re.findall("^From", fhand)
     except:
        print('skip')
     if p == i:
         print('YAY!!!')
         file += 1         
 print('mbox.txt had',file,'lines that matched:',stuff)