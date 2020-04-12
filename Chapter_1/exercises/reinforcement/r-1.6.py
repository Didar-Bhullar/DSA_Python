# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def odd_sum_squares(n):
    total = 0
    for value in range(n):
        if (value % 2) == 1:
            total += pow(value, 2)
    return total

assert(odd_sum_squares(3) == 1)