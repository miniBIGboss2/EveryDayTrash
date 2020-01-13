"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

main_list = []


def make_list():
    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, 1000)):
            n = x * y
            temp = n
            rev = 0
            while n > 0:
                dig = n % 10
                rev = rev * 10 + dig
                n = n // 10
            if temp == rev:
                main_list.append(temp)
                break


make_list()
main_list.sort()
print(main_list[-1])
