# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

def make_list():
    return list(range(8, -9, -2))

my_list = [8, 6, 4, 2, 0, -2, -4, -6, -8]
assert(make_list() == my_list)