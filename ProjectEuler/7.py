"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

import time


def prime():
    number_of_primes = 0
    number_to_check = 2
    number_of_dividers = 0
    while number_of_primes <= 10001:
        for i in range(1, number_to_check):
            if number_to_check % i == 0 and number_of_dividers != 3:
                number_of_dividers += 1
            elif number_of_dividers == 3:
                number_of_dividers = 0
                number_to_check += 1
                break
            elif i == number_to_check - 1 and number_of_dividers == 2:
                number_to_check += 1
                number_of_primes += 1
        print(number_to_check)
        print(number_of_primes)


start_time = time.time()
prime()
print(time.time() - start_time)
