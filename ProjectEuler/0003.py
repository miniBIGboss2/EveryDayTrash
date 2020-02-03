"""The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143  ?"""

# Построить функцию с автоматическим поиском простых чисел и подстроить ее в поиск

testNumb = 1000
PrimeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
AutoPrime = []
first_numb = 600851475143


def look_for_prime(x, y):

    while True:
        if x % y == 0 and y != 1:
            AutoPrime.append(y)
            y += -1
            print(y)
        elif x % y != 0 and y != 1:
            y += -1
            print(y)
        else:
            print(AutoPrime)
            break

    for x in AutoPrime:
        if x % 5 == 0:
            AutoPrime.remove(x)

    for x in AutoPrime:
        if x % 3 == 0:
            AutoPrime.remove(x)

    for x in AutoPrime:
        if x % 2 == 0:
            AutoPrime.remove(x)


def func5(x):
    if x % 5 == 0:
        return 0
    else:
        return 1


def func7(x):
    if x % 7 == 0:
        return 0
    else:
        return 1


def func13(x):
    if x % 13 == 0:
        return 0
    else:
        return 1


def is_prime(u):
    for x in PrimeNumbers:
        if u % x == 0:
            print(x)


look_for_prime(600851475143, 600851475143)
print(AutoPrime)
b = filter(func5, AutoPrime)
b = list(b)
print(b)
b = filter(func7, b)
b = list(b)
print(b)
b = filter(func13, b)
b = list(b)
print(b)
