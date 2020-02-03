"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

# todo 405

import time


def prime():
    number_of_primes = 1
    number_to_check = 2
    number_of_dividers = 0
    while number_of_primes <= 10001:
        for i in range(1, number_to_check + 1):
            if number_to_check % i == 0:
                number_of_dividers += 1
                if number_of_dividers == 2 and i != number_to_check:
                    number_of_dividers = 0
                    number_to_check += 1
                elif number_of_dividers == 2 and i == number_to_check:
                    number_of_dividers = 0
                    print(number_to_check)
                    number_to_check += 1
                    print(number_of_primes)
                    number_of_primes += 1


start_time = time.time()
prime()
print(time.time() - start_time)
