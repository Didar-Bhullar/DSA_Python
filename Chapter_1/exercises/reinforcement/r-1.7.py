# Give a single command that computes the sum from Exercise R-1.6, 
# relying on Python’s comprehension syntax and the built-in sum function

def odd_sum_squares(n):
    return sum([pow(n, 2) for n in range(n) if n % 2 == 1 ])


assert(odd_sum_squares(4) == 10)