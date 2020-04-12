# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

def produce_list():
    return [pow(2, x) for x in range(9)]

assert(produce_list() == [1,2,4,8,16,32,64,128,256])