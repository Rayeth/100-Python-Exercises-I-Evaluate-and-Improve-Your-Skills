#Question: Create a function that takes any string as input and returns the number of words for that string.

def splitter(strng):
    words = len(strng.split())
    return words
print(splitter('Hello my friends!'))
