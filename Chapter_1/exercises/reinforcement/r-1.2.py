# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    value_plus_two = None
    for value in range(0,k+1,2):
       if value == k:
           return True
    return False

def is_even_bitwise(k):
    result = (k & 1)
    if result == 1:
        return False
    else:
        return True



assert(is_even(5) == False)
assert(is_even(4) == True)
assert(is_even(1) == False)

assert(is_even_bitwise(5) == False)
assert(is_even_bitwise(4) == True)
assert(is_even_bitwise(1) == False)
