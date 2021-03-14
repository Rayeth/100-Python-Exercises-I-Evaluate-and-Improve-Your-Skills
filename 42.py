#Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

zipped_lists = zip(a, b)

sum = [x + y for (x, y) in zipped_lists]

for  item in sum:
    print(item)

# for i, j in zip(a, b):
#     print(i + j)