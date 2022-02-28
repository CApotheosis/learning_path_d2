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


class C(A, B):
    def mro(self):
        return [C, A, B, object]


obj = C()
obj.mro()
# obj.process()
