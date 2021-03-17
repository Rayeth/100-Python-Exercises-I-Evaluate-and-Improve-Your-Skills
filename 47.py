# Conditioned letter extractor
# Iterates thru 26 txt files then scrip checksi f the letter inside is a leetter of a string 'python'

import glob

letters = []
strng = 'python'
file_list = glob.glob("letters/*.txt")
for filename in file_list:
    with open(filename, 'r') as file:
        x = file.read().strip()       
        if x in strng:
            letters.append(x)

print(letters)
print(file_list)