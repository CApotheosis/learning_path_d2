def func():
    a = 10

    def wrapper():
        # nonlocal a # to access write option
        a = 20
        print("wrapper", a)

    wrapper()
    print("func", a)


func()

l = [i for i in range(20)]
# lambda x, y: x+1+y, x, y
# map(func, iterable)
mapped = list(map(lambda x: x ** 2, l))
print(mapped)
filtered = list(filter(lambda x: x % 2 == 0, l))
print(filtered)


# from functools import reduce

# def sum(acc, x):
#   return x

# reduced = reduce((lambda acc, y: acc + y), l, 10)
# print(reduced)


# def func_1(a, b=3, /):
#     pass


# func_1(1, 2, depth=3)

# def func_2(a, *args, **kwargs):
#     pass

# func_2(length=2, depth=3)


def do(a, /, b, c=3, *d, e, f=6, **g):
    print(a, b, c, d, e, f, g)


# do(1, 2, 3, 4, 5, 6, e=3)
# do(1, 2, a=123, t=234, e=345) # order is important


def function_ex(a, b=None):
    if b is None:
        b = []

    b.append(a)  # 23124231
    return b


res = function_ex(1)  # 23124231
print("res", res)
res = function_ex(2)
print(res)


def rec(a):
    if a == 10:
        return a

    return rec(a) + rec(a)

# namedtuple 
# module names

from contextlib import contextmanager
from functools import wraps
import queue

def decorator_factory(*args, **kwargs):
    print(args, kwargs)
    def func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
            print("end")
      
        return wrapper
    return func


@decorator_factory(a=2, b=3)
def hello(h):
    """Print whatewer you pass."""
    print(h)


hello("dsadas")
# a = decorator_factory(1, 2, 4)(hello)
# a("Hello world")
# print(a.__name__, a.__doc__)
print(hello.__name__, hello.__doc__)



class A:
    def __hash__(self):
        return 1

a = A()
print(hash(a))


print()
x = 4

def func(a, c, d=32, *arg, name='name', log='log', **kwargs):
    # global x
    x = 20 
    print(x)
    def nested(start):
        nonlocal x 
        print(x, start)
    
    return nested

t = func(2, 3, [2,3,4], name="Ya")
t(12)

def dec_base(name):
    def dec(func):
        def wrapper(*args, **kwargs):
            print("Start", args)
            func(*args, **kwargs)
            print("end")

        return wrapper
    return dec


# @dec_base
def hello(a, b, c):
    print("Greetings")

# hello(1, 2, 3)
a = dec_base("user")
a(hello)(2, 3, 4)
# a = dec(func)
# a()


class Accesss:
    a = 2

    def __init__(self, name, psw):
        self.name = name
        self.psw = psw

    @staticmethod
    def get_value():
        print("gets value")

    @classmethod
    def func(cls, new_name):
        cls.name = new_name
        return cls(new_name, "Name")

    def __str__(self) -> str:
        return f"{self.name}, {self.psw}"

a = Accesss('2', "Adam")
a_1 = Accesss('2', "Joe")
Accesss.get_value()
print(Accesss.func("Rose"))
a.func("new name")
print(a)

class Player:
    """classmethod is likely to self, but instead of self we use cls keyword to reference class
    classmethod can be used without intanciating class and creatin __init__ dunder method
    """
    arr = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} {self.age}"

    @classmethod
    def add_nums(cls, num_1, num_2):
        return num_1 + num_2

    # intanciating an object with cls
    @classmethod
    def get_player_age(cls, num_1, num_2, a):
        cls.a = a
        return cls("Clark", num_1 + num_2) # Here, we can override basic __init__ - method with cls

    @staticmethod
    def add_nums_2(num_1, num_2):
        return num_1 + num_2

print(Player.add_nums(1, 4))
player = Player("Joe", 43)
print(player)
player_1 = Player(20, 30)
print(player_1.get_player_age(1, 2, "aaaa"))
print("player_1", player_1, player_1.name, player_1.age, player_1.a)


# try:
#     open()
# finally:
#     close()

@contextmanager
def func():
    # open
    yield 
    # close


class A:
    def __enter__(self):
        pass

    def __exit__(self, type, msg, trb):
        pass


l = [1,2,3]
s = iter(l)
a = iter(s)
print(a, s)
next(s)


for var in [1,2,3,4]:
    pass

def func():
    for i in range(10):
        yield i

for val in []:
    print(val) 
else:
    print("worked")


l = [12,2,3]
i = 0


while i < len(l):
    print(l[i])
    i += 1  
else:
    print("worked")

l = [x for x in range(100) if 1 > 2]


class CustomException(BaseException):
    """Custom Exception."""
    pass

# raise CustomException

# Garbage collection (gc) generation
0
1
2

"""
# for data exchange in multiprocessing
# pipes 
# shared_memory 
# queue - Queues are a great way of sending small data to and from multiple processes.

# lock 
# semaphore - sets lock and limitation to running processes
# event (queue)
# condition 
# bareer

# Sprint Planning
# Daily Scrum
# Sprint Review
# Sprint Retrospective
# Product Backlog Refinement
# Backlog grooming

# agile artifacts


# story point 

S - Single-responsiblity Principle
A class should have one and only one reason to change, 
meaning that a class should have only one job.

O - Open-closed Principle
Objects or entities should be open for extension but closed for modification.

L - Liskov Substitution Principle
Let q(x) be a property provable about objects of x of type T. 
Then q(y) should be provable for objects y of type S where S is a subtype of T.

I - Interface Segregation Principle
D - Dependency Inversion Principle
"""
from functools import wraps
def arg_dec(a):
    print(a)
    def dec(func):
        @wraps(func)
        def a():
            """Docs 3"""
            print("do smth")
            func()
            print("end smth")
        return a
    return dec

@arg_dec(2)
def hello():
    """My doc"""
    print("hello")

hello()
print(hello.__doc__)

class P:
    def a(self):
        print("yes")

    def a(self):
        print("no")

a = P()
a.a()