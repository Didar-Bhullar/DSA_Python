# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n

def sum_of_squares(n):
    total = 0
    for value in range(n):
        total += pow(value, 2) 
    return total


assert(sum_of_squares(4) == 14)
