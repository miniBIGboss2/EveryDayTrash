"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

import time

temp_list = []


def my_func():
    number_to_check = 2
    number_of_dividers = 0
    while number_to_check < 10:
        for i in range(1, number_to_check + 1):
            if number_to_check % i == 0:
                number_of_dividers += 1
                if number_of_dividers == 2 and i != number_to_check:
                    number_of_dividers = 0
                    number_to_check += 1
                elif number_of_dividers == 2 and i == number_to_check:
                    number_of_dividers = 0
                    print(number_to_check)
                    temp_list.append(number_to_check)
                    number_to_check += 1


start_time = time.time()
my_func()
print(sum(temp_list))
print(time.time() - start_time)
