from tkinter import E


def func(o):
    try:
        o["a"] = 1/0
    except Exception as err:
        print(err)

o = {"a": 1, "b": 1}
d = {}
d = func(o)

print(o)


class A:
    def process(self):
        print('A process()')


class B(A):
    def process(self):
        print('B process()')


# class C(A, B):
#     def mro(self):
#         return [C, A, B, object]

# obj = C()
# obj.mro()
# obj.process()

a, *_, b = 1,2,3,4,5
print(a, b, *_)


def func(c):
    print(c)


func("dsadasd", **{})

def num(*args):
    print(args)

num(1, 2, 3, 4)

import pydantic
print('compiled:', pydantic.compiled)

