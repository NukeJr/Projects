fruit = 'banana'
print(fruit[0:7])

l = input(f"Write a word: ")
s = 'L' + l[1:]
print(s)

print(fruit[:3])
print(fruit[3:])

l = 'landon'
s = 'L' + 'landon'[1:]
print(s)

count = 0
for c in fruit:
    if c == 'n':
        count = count + 1
print("There are:",count)
print("many ns.")


stuff = 15
dir(stuff)































index = -1
while index <= abs(len(fruit)):
    letter = fruit[index]
    print(letter)
    index = index - 1
    
stuff = 15
dir(stuff)
