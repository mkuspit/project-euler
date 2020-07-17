"""
Problem 10: Largest prime factor
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

#%% Brute force solution - doesn't work
def sum_prime_numbers(my_number):
    def is_prime(m):
        if m <= 1:
            return False
        for i in range(2, m):
            if m % i == 0:
                return False
        return True

    prime_numbers = []

    for n in range(2, my_number):
        if is_prime(n):
            prime_numbers.append(n)
    
    return sum(prime_numbers)

print(sum_prime_numbers(2000000))