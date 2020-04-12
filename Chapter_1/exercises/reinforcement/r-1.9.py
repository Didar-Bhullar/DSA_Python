# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

def create_number_range():
    return list(range(50,81,10))

assert(create_number_range() == [50,60,70,80])