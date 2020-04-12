# Give a single command that computes the sum from Exercise R-1.4, 
# relying on Python’s comprehension syntax and the built-in sum function.

def list_compre_sum(n):
    return sum([pow(n, 2) for n in range(n)])

assert(list_compre_sum(4) == 14)
