# make oneline code
def get_max_repeated_value(numbers):
    return max(((numbers.count(val), val) for val in set(numbers)))[1]

numbers = [1, 2, 3, 4, 2, 3, 2, -1, -1, -1, -1]
print(get_max_repeated_value(numbers))
