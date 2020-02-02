"""The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

"""

import time


def my_func():
    start_numb = 13
    temp_start_numb = start_numb
    my_list = [start_numb]
    while True:
        if temp_start_numb % 2 == 0:
            temp_numb = int(temp_start_numb / 2)
            my_list.append(temp_numb)
            temp_start_numb = temp_numb
            if temp_numb == 1:
                print(my_list)
                print(len(my_list))
                print(start_numb)
                return False
        else:
            temp_numb = 3 * temp_start_numb + 1
            my_list.append(temp_numb)
            temp_start_numb = temp_numb


def test_my_func():
    start_numb = 13
    temp_start_numb = start_numb
    my_list = [start_numb]
    while True:
        if temp_start_numb % 2 == 0:
            temp_numb = int(temp_start_numb / 2)
            my_list.append(temp_numb)
            temp_start_numb = temp_numb
            if temp_numb == 1:
                print(my_list)
                print(len(my_list))
                print(start_numb)
                return False
        else:
            temp_numb = 3 * temp_start_numb + 1
            my_list.append(temp_numb)
            temp_start_numb = temp_numb


start_time = time.time()
my_func()
test_my_func()
print(time.time() - start_time)
