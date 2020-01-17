"""The sum of the squares of the first ten natural numbers is, 1**2+2**2+...+10**2=385
The square of the sum of the first ten natural numbers is, (1+2+...+10)**2=55**2=3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import time


def both():
    power_num = 0
    sum_num = 0
    for i in range(1, 101):
        power_num += i ** 2
        sum_num += i
    sum_num = sum_num ** 2
    print(sum_num - power_num)


start_time = time.time()
both()
print(time.time() - start_time)
