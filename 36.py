#Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

# def splitter(strng, file_to_open):

#     f = open(file_to_open, 'r')

#     file_contents = f.read()
#     words = len(file_contents.split())
#     return words


# f = open('words1.txt', 'r')

# file_contents = f.read()

# print(splitter(file_contents,'words1.txt'))

# f.close()

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split()
        return len(strng_list)

print(count_words('words1.txt'))