"""
Problem 5: Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#%% Solution
def list_prime_factors(my_number):
    prime_factors = []
    i = 2
    while my_number != 1:
        while my_number % i != 0:
            i += 1
        my_number /= i
        prime_factors.append(i)
        i = 2
    return prime_factors


for n in range(2, 20):
    print(list_prime_factors(n))

# Answer: