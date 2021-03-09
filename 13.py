#Question: Complete the script, so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.

my_range = range(1, 21)

# my_list = [str(num) for num in my_range]

# print(my_list)

my_list = list(map(str, my_range))
print(my_list)