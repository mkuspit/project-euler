"""
Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
#%% Simple solution
# my_list = []
# for n in range(1000):
#     if (n % 3 == 0) or (n % 5 == 0):
#         my_list.append(n)
# result = sum(my_list)
# print(result)

#%% Elegant solution
def find_the_sum(number_below, list_of_numbers):
    my_list = []
    for n in range(number_below):
        for m in list_of_numbers:
            if (n % m == 0) and (n not in my_list):
                my_list.append(n)
    return sum(my_list)

print(find_the_sum(1000, [3, 5]))
# Answer: 233168