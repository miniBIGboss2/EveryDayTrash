"""The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600 851 475 143 ?"""


def compute():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return str(n)


def smallest_prime_factor(n):
    for i in range(2, 600851475143):
        if n % i == 0:
            return i
    return n


print(compute())
