"""
Problem 7: 10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
#%% Solution
def nth_prime_number(n):
    def is_prime(m):
        if m <= 1:
            return False
        for i in range(2, m):
            if m % i == 0:
                return False
        return True
    
    q = 0
    q_count = 0
    while q_count < n:
        q += 1
        if is_prime(q):
            q_count += 1
    return q

print(nth_prime_number(10001))
# Answer: 104743