"""The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million."""

import time


def my_func():
    count = 13
    chain_len = 0
    temp_chain_len = 0
    while count < 1000000:
        temp_numb = count
        while True:
            if temp_numb % 2 == 0:
                temp_numb = temp_numb / 2
                temp_chain_len += 1
                if temp_numb == 1:
                    if temp_chain_len >= chain_len:
                        chain_len = temp_chain_len
                        temp_chain_len = 0
                        print(count)
                        count += 1
                        break
                    else:
                        temp_chain_len = 0
                        count += 1
                        break
            else:
                temp_numb = 3 * temp_numb + 1
                temp_chain_len += 1


start_time = time.time()
my_func()
print(time.time() - start_time)
