#Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

import string

# alpahbet_li = []
# for letter in string.ascii_lowercase:
#     alpahbet_li.append(letter)  

# alphabet = '\n'.join(alpahbet_li)

# with open('alphabet.txt', 'w') as file:
    
#     strng = file.write(alphabet)

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")