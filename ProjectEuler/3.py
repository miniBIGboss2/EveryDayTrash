"""The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143  ?"""

# Построить функцию с автоматическим поиском простых чисел и подстроить ее в поиск

testNumb = 1000
PrimeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
AutoPrime = [2, ]
endNumb = 600851475143


for i in range(0, 13195):
    if i % 2 != 0 and i != 1:
        AutoPrime.append(i)

for i in AutoPrime:
    if i % 3 == 0 and i != 3:
        AutoPrime.remove(i)

for i in AutoPrime:
    if i % 5 == 0 and i != 5:
        AutoPrime.remove(i)

for i in AutoPrime:
    floatTest = 13195 / i
    if type(floatTest) is float:
        AutoPrime.remove(i)


print(AutoPrime[-1])

def is_prime(i):
    for x in PrimeNumbers:
        if i % x == 0:
            print(x)


print(AutoPrime)
