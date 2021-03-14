

import os

signs = []

directory = r'C:\Users\nopa\OneDrive - H. Lundbeck A S\Desktop\Git\100-Python-Exercises-I-Evaluate-and-Improve-Your-Skills\letters'



for filename in os.listdir(directory):
    with open(directory + '\\' + filename, 'r') as file:
        signs.append(file.read())

print(signs)