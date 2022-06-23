import math


import math
import sys

# print(sys.modules)

try:
    file = open("hello.txt", mode="w")
    file.write("ASdsdad")
except Exception as err:
    pass
finally:
    file.close()

# with file:
#     file.write("Hello, World!")

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
