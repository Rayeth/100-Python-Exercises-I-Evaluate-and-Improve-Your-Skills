# Question: Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

# Expected output: 

# Hello
# Hello
# Hello
# Hello
# End of Loop

import time

prog_sleep = 0

while prog_sleep < 4:
    prog_sleep += 1
    print('Hello')
    time.sleep(prog_sleep)
else:
    print('End of Loop')

# i = 0
# while True:
#     print('Hello')
#     i = i +1
#     if i> 3:
#         print('End of Loop')
#         break
#     time.sleep(i)
    