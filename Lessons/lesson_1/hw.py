# make oneline code
def get_max_repeated_value(numbers):
    # return max(((numbers.count(val), val) for val in set(numbers)))[1]
    return max(numbers, key=numbers.count)


numbers = [1, 2, 3, 4, 2, 3, 2, -1, -1, -1, -1]
print(get_max_repeated_value(numbers))

import dis
import math
import hashlib # generate hash according algorithms md5, sha

dis.dis(get_max_repeated_value)
print(1.5 // 2) # the rounding goes towards minus infinity part
print(math.floor(1 / 2)) # ceil is upper floor is down

# Set
# Like other collections, sets support x in set, len(set), 
# and for x in set. Being an unordered collection, sets 
# do not record element position or order of insertion. 
# Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.
# print(dir(set))
# Frozenset.
# Return a new set or frozenset object whose elements are taken from iterable.
# print(dir(frozenset))

"""Hashable.

    An object is hashable if it has a hash value which never 
    changes during its lifetime (it needs a __hash__() method), 
    and can be compared to other objects (it needs an __eq__() method). 
    Hashable objects which compare equal must have the same hash value.
    
    Reference: https://www.programiz.com/python-programming/methods/built-in/hash
    hash()
    As stated above, hash() method internally calls __hash__() method. 
    So, any objects can override __hash__() for custom hash values.
"""
# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:',hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))

class A:
    def __init__(self, a):
        self.a = a

p = A(1)
print(p.__hash__()) # return an id

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        print("other", other)
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

person = Person(1, 'Adam')
print("hash", hash(person.name), hash(person.age), person.__eq__(Person(1, 'Adam')))
