import os

# Get the file path
folder_path = os.path.dirname(__file__)
file_name = os.path.join(folder_path, "mbox-short.txt")

# Open the file using 'with' to ensure proper file handling
with open(file_name) as fhand:
    many = dict()

    # Iterate through each line in the file
    for line in fhand:
        if line.startswith('From '):  # Ensure the line starts with 'From '
            words = line.split()  # Split the line by spaces
            if len(words) > 1:  # Make sure we have an email address (second word)
                email = words[1]  # Get the second word (email address)
                domain = email.split('@')[-1]  # Get the domain part after '@'
                many[domain] = many.get(domain, 0) + 1  # Count the occurrences

# Print the dictionary of email domains and their counts
print(many)
