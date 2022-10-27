"""
import math


import math
import sys

print(sys.modules)

try:
    file = open("hello.txt", mode="w")
    file.write("ASdsdad")
except Exception as err:
    pass
finally:
    file.close()

with file:
    file.write("Hello, World!")

# Usage of with statement
import pathlib

file_path = pathlib.Path("hello.txt")

with file_path.open("w") as file: # None
    file.write("Hello, World!")


from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 42
    print(Decimal("1") / Decimal("42"))

print(Decimal("1") / Decimal("42"))


# as function
from contextlib import contextmanager

@contextmanager
def hello_context_manager():
    print("Entering the context...")
    yield "Hello, World!"
    print("Leaving the context...")

with hello_context_manager() as hello:
    print(hello)
    # code ....

class A:
    def __enter__(self):
        print("Entering the context...")
        return "AAAAA"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving the context...")

from math import ceil
# finders and loaders


# another file
from file import ceil


import dis 

def func():
    return 1
    return 2


print(dis.dis(func))


class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")

# exception will occur
with HelloContextManager() as hello:
    print(hello)
    hello[100]
"""

# Handling Exceptions in a Context Manager
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            print(f"Exception traceback: {exc_tb}")
            return True

with HelloContextManager() as hello:
    print(hello)
    hello[100]

print("works")
