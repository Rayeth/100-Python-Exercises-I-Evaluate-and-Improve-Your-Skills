# Letter extractor
# From 26 files we created in previous exercies
# Export them to list and print it

import glob

letters = []

file_list = glob.glob("letters/*.txt")
for filename in file_list:
    with open(filename, 'r') as file:
        letters.append(file.read())

print(letters)

