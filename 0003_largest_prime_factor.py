"""
Problem 3: Largest prime factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
#%% Brute force solution
# def max_prime_factor(my_number):
#     def is_prime(m):
#         if m <= 1:
#             return False
#         for i in range(2, m):
#             if m % i == 0:
#                 return False
#         return True
#
#     prime_factors = []
#     for n in range(2, int(my_number/2)):
#         if (my_number % n == 0) and is_prime(n):
#             prime_factors.append(n)
#
#     return max(prime_factors)
#
# print(max_prime_factor(600851475143))

#%% Smarter solution
def max_prime_factor(my_number):
    prime_factors = []
    i = 2
    while my_number != 1:
        while my_number % i != 0:
            i += 1
        my_number /= i
        prime_factors.append(i)
        i = 2
    return max(prime_factors)

print(max_prime_factor(600851475143))
# Answer: 6857
