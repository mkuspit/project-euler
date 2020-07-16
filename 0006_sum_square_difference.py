"""
Problem 6: Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#%% Solution
def find_the_difference(my_number):
    numbers = []
    squares = []
    for n in range(1, my_number + 1):
        numbers.append(n)
        squares.append(n**2)
    result = sum(numbers)**2 - sum(squares)
    return result
    
print(find_the_difference(100))
# Answer: 25164150