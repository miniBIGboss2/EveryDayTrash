"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# Todo Time to execute 39min

import time

just_list = []


def shit():
    numb = 1
    check = 0
    while True:
        for i in range(1, 21):
            if numb % i == 0:
                check += 1
                print(numb)
                if check == 20:
                    just_list.append(numb)
                    return False
            else:
                numb += 1
                check = 0
                print(numb)


start_time = time.time()
shit()
print(just_list)
print(time.time() - start_time)
