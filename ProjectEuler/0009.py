"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

import time
import math


def my_func():
    c = 0
    while True:
        for a in range(1, 1000):
            for b in range(1, 1000):
                temp = a ** 2 + b ** 2
                c = math.isqrt(temp)
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print(a, b, c)
                    print(a*b*c)
                    return False


start_time = time.time()
my_func()
print(time.time() - start_time)
