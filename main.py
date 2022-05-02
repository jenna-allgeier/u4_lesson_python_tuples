def create_tuple(list_of_nums):
    # Create a tuple from a list and return it.
    my_tup = tuple(list_of_nums)
    return my_tup


def get_value(tup):
    # Return the 3rd value in the provided tuple
    return tup[2]


def get_values(tup):
    # return the values from index 1-3
    # 3 should be inclusive
    return tup[1:4]


def get_max(tup):
    # return the largest number in the provided tuple
    return max(tup)

