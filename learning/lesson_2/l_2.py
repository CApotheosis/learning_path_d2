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
print(res)
res = function_ex(2)
print(res)


def rec(a):
    if a == 10:
        return a

    return rec(a) + rec(a)


from functools import wraps

def decorator_factory(*args, **kwargs):
    print(args, kwargs)
    def func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
            print("end")
      
        return wrapper
    return func


# @decorator_factory(a=2, b=3)
def hello(h):
    """Print whatewer you pass."""
    print(h)


# hello("dsadas")
a = decorator_factory(1, 2, 4)(hello)
a("Hello world")
print(a.__name__)
