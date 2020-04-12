# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    min_number = data[0]
    max_number = data[0]

    for val in data[1:]:
        if min_number > val:
            min_number = val
        if max_number < val:
            max_number = val
    
    return (min_number, max_number)


assert(minmax([1,2,3]) == (1,3))
assert(minmax([-1, 15, -3, 99, 220]) == (-3, 220))
assert(minmax([-1, 15, -3, 99, 220]) != (-1, 220))
